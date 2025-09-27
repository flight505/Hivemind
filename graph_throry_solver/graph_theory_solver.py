import random
import json
import asyncio
import heapq
from collections import defaultdict, deque
from termcolor import colored
from openai import AsyncOpenAI
import os
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Configuration variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "x-ai/grok-code-fast-1"
NUM_GRAPHS = 5
NUM_NODES = 28  # Number of nodes in each graph
MAX_WEIGHT = 20  # Maximum edge weight
REASONING_EFFORT = "high"

def setup_openai_client():
    """Set up the OpenAI client for OpenRouter"""
    return AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

def generate_random_graph():
    """
    Generate a random connected undirected graph with positive weights
    Returns adjacency list and string representation
    """
    nodes = list(range(NUM_NODES))
    edges = []

    # Ensure the graph is connected by creating a spanning tree first
    # Start with a random spanning tree
    used_nodes = {0}  # Start with node 0
    unused_nodes = set(nodes[1:])

    # Add edges to connect all nodes
    while unused_nodes:
        from_node = random.choice(list(used_nodes))
        to_node = random.choice(list(unused_nodes))
        weight = random.randint(1, MAX_WEIGHT)
        edges.append((from_node, to_node, weight))
        used_nodes.add(to_node)
        unused_nodes.remove(to_node)

    # Add some additional random edges to make it more interesting
    # Add up to NUM_NODES extra edges
    for _ in range(random.randint(0, NUM_NODES)):
        u = random.randint(0, NUM_NODES - 1)
        v = random.randint(0, NUM_NODES - 1)
        if u != v and not any((u == e[0] and v == e[1]) or (u == e[1] and v == e[0]) for e in edges):
            weight = random.randint(1, MAX_WEIGHT)
            edges.append((u, v, weight))

    # Create adjacency list
    adj_list = defaultdict(list)
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))  # Undirected graph

    # Create string representation for LLM
    edge_strings = []
    for u, v, w in sorted(edges):  # Sort for consistent ordering
        edge_strings.append(f"{u}-{v}:{w}")

    graph_str = ", ".join(edge_strings)

    # Choose random start and end nodes (different from each other)
    start_node = random.randint(0, NUM_NODES - 1)
    end_node = random.randint(0, NUM_NODES - 1)
    while end_node == start_node:
        end_node = random.randint(0, NUM_NODES - 1)

    return adj_list, graph_str, start_node, end_node, edges

def dijkstra_shortest_path(adj_list, start, end):
    """
    Compute shortest path using Dijkstra's algorithm
    Returns distance and path
    """
    distances = {node: float('infinity') for node in range(NUM_NODES)}
    distances[start] = 0
    previous = {node: None for node in range(NUM_NODES)}

    priority_queue = [(0, start)]  # (distance, node)
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            break

        for neighbor, weight in adj_list[current_node]:
            if neighbor in visited:
                continue

            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    # Reconstruct path
    if distances[end] == float('infinity'):
        return float('infinity'), []  # No path exists

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[end], path

def save_graph_visualization(edges, graph_num, start_node, end_node, correct_path=None, timestamp=None):
    """
    Save a visualization of the graph as an image file
    """
    # Create NetworkX graph
    G = nx.Graph()

    # Add edges with weights
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Create positions using spring layout for better visualization
    pos = nx.spring_layout(G, seed=42, k=1.5)  # k controls spacing

    plt.figure(figsize=(12, 8))

    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500, alpha=0.8)

    # Draw edges with weights
    edges_list = list(G.edges())
    weights = [G[u][v]['weight'] for u, v in edges_list]
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')

    # Draw edge labels (weights)
    edge_labels = {(u, v): w for u, v, w in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10, font_color='red')

    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Highlight start and end nodes
    start_color = 'green'
    end_color = 'red'

    # Draw start node
    nx.draw_networkx_nodes(G, pos, nodelist=[start_node],
                          node_color=start_color, node_size=600, alpha=0.9)

    # Draw end node
    nx.draw_networkx_nodes(G, pos, nodelist=[end_node],
                          node_color=end_color, node_size=600, alpha=0.9)

    # Highlight correct path if provided
    if correct_path:
        path_edges = [(correct_path[i], correct_path[i+1]) for i in range(len(correct_path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                              width=4, edge_color='blue', alpha=0.8)

    # Add title and legend
    title = f"Graph {graph_num}: Start={start_node} (green), End={end_node} (red)"
    if correct_path:
        title += f"\nCorrect Path: {' -> '.join(map(str, correct_path))}"
    plt.title(title, fontsize=14, pad=20)

    # Add legend
    legend_elements = [
        plt.Rectangle((0,0),1,1, facecolor='lightblue', alpha=0.8, label='Regular Nodes'),
        plt.Rectangle((0,0),1,1, facecolor='green', alpha=0.9, label='Start Node'),
        plt.Rectangle((0,0),1,1, facecolor='red', alpha=0.9, label='End Node')
    ]
    if correct_path:
        legend_elements.append(plt.Rectangle((0,0),1,1, facecolor='blue', alpha=0.8, label='Shortest Path'))

    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))

    plt.axis('off')
    plt.tight_layout()

    # Create filename
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"graph_{graph_num}_{timestamp}.png"

    # Save the plot
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

    return filename

def parse_llm_response(response):
    """
    Parse LLM's shortest path response
    Expected format: "Distance: X, Path: A->B->C"
    """
    if not response:
        return None, []

    # Clean up response
    response = response.strip()

    try:
        # Look for distance and path
        distance = None
        path = []

        # Find distance
        if "distance:" in response.lower():
            distance_part = response.lower().split("distance:")[1].split(",")[0].strip()
            distance = int(distance_part)

        # Find path
        if "path:" in response.lower():
            path_part = response.lower().split("path:")[1].strip()
            # Extract numbers from path like "0->1->2->3"
            path_numbers = []
            for part in path_part.replace("->", " ").split():
                try:
                    path_numbers.append(int(part.strip("(),")))
                except ValueError:
                    continue
            path = path_numbers

        return distance, path

    except Exception as e:
        print(colored(f"Error parsing response: {e}", "red"))
        return None, []

def validate_shortest_path(llm_distance, llm_path, correct_distance, correct_path):
    """
    Validate LLM's shortest path solution
    """
    try:
        # Check if distance matches
        if llm_distance != correct_distance:
            print(colored(f"Distance mismatch: LLM={llm_distance}, Correct={correct_distance}", "red"))
            return False

        # Check if path is valid (same start and end, same length or valid alternative)
        if not llm_path or llm_path[0] != correct_path[0] or llm_path[-1] != correct_path[-1]:
            print(colored(f"Path endpoints mismatch: LLM path={llm_path}, Correct path={correct_path}", "red"))
            return False

        # For undirected graphs, multiple paths might have same distance
        # So we mainly check distance and endpoints
        print(colored(f"Path validation: Distance correct, endpoints match", "green"))
        return True

    except Exception as e:
        print(colored(f"Validation error: {e}", "red"))
        return False

async def ask_llm_shortest_path(client, graph_str, start_node, end_node):
    """Send a graph shortest path question to the LLM"""
    try:
        question = f"Find the shortest path from node {start_node} to node {end_node} in this graph: {graph_str}"
        print(colored(f"Asking: {question}", "cyan"))

        prompt = f"""Find the shortest path from node {start_node} to node {end_node} in this undirected weighted graph.

Graph edges (format: node1-node2:weight): {graph_str}

🚫 ABSOLUTELY FORBIDDEN: Do NOT use any advanced algorithms or formulas!
❌ NO Dijkstra's algorithm
❌ NO Bellman-Ford algorithm  
❌ NO Floyd-Warshall algorithm
❌ NO A* search
❌ NO any graph algorithms you've memorized
❌ NO shortcuts or optimizations

✅ REQUIRED: Use ONLY basic methods:
- Start from the source node
- Explore neighbors step by step
- Keep track of visited nodes
- Update distances manually
- Choose the unvisited node with smallest current distance
- Work through the graph systematically

⚠️ CRITICAL: You MUST explore the graph manually without using any named algorithms!

RESPONSE FORMAT: Respond with EXACTLY this format (no extra text):
Distance: [number], Path: [start]->[node]->[node]->[end]

Example: Distance: 15, Path: 0->2->5->3

Find the shortest path: {question}"""

        completion = await client.chat.completions.create(
            model=MODEL_NAME,
            reasoning_effort=REASONING_EFFORT,
            messages=[
                {
                    "role": "system",
                    "content": """CRITICAL GRAPH SEARCH RULES - YOU MUST FOLLOW THESE EXACTLY:

🚫 ABSOLUTELY FORBIDDEN: Do NOT use ANY named graph algorithms:
❌ DO NOT use Dijkstra's algorithm
❌ DO NOT use Bellman-Ford algorithm
❌ DO NOT use Floyd-Warshall algorithm  
❌ DO NOT use A* search
❌ DO NOT use breadth-first search (BFS)
❌ DO NOT use depth-first search (DFS)
❌ DO NOT use any shortest path algorithms
❌ DO NOT use any memorized graph traversal methods

✅ REQUIRED: Only use basic systematic exploration:
- Start from source node with distance 0
- Examine each node's neighbors one by one
- Keep a list of visited nodes
- Track current best distance to each node
- When at a node, check all its unvisited neighbors
- Update distances if you find a shorter path
- Choose which node to explore next based on smallest known distance
- Continue until you reach the target or exhaust all possibilities

⚠️ WARNING: If you use ANY named algorithm, your answer will be marked WRONG.
You MUST explore the graph manually and systematically."""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        response = completion.choices[0].message.content
        print(colored(f"Raw response: {repr(response)}", "cyan"))
        return response
    except Exception as e:
        print(colored(f"Error asking question: {e}", "red"))
        return None

async def process_single_graph(client, graph_num, adj_list, graph_str, start_node, end_node, edges):
    """Process a single graph asynchronously"""
    print(colored(f"\nGraph {graph_num}:", "yellow"))
    print(colored(f"Graph: {graph_str}", "green"))
    print(colored(f"Start: {start_node}, End: {end_node}", "blue"))

    # Compute correct shortest path
    correct_distance, correct_path = dijkstra_shortest_path(adj_list, start_node, end_node)
    print(colored(f"Correct distance: {correct_distance}", "magenta"))
    print(colored(f"Correct path: {'->'.join(map(str, correct_path))}", "magenta"))

    # Generate and save graph visualization
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    viz_filename = save_graph_visualization(edges, graph_num, start_node, end_node, correct_path, timestamp)
    print(colored(f"Graph visualization saved: {viz_filename}", "green"))

    # Ask LLM to find shortest path
    llm_response = await ask_llm_shortest_path(client, graph_str, start_node, end_node)

    if llm_response:
        print(colored(f"LLM Response: {llm_response}", "cyan"))

        # Parse LLM response
        llm_distance, llm_path = parse_llm_response(llm_response)
        print(colored(f"Parsed - Distance: {llm_distance}, Path: {llm_path}", "cyan"))

        # Validate the answer
        is_correct = validate_shortest_path(llm_distance, llm_path, correct_distance, correct_path)

        status = "✓ CORRECT" if is_correct else "✗ WRONG"
        color = "green" if is_correct else "red"

        print(colored(f"Validation: {status}", color))

        return {
            "graph_number": graph_num,
            "graph_edges": edges,
            "graph_string": graph_str,
            "start_node": start_node,
            "end_node": end_node,
            "correct_distance": correct_distance,
            "correct_path": correct_path,
            "llm_response": llm_response,
            "llm_distance": llm_distance,
            "llm_path": llm_path,
            "is_correct": is_correct,
            "visualization_file": viz_filename
        }
    else:
        print(colored("No response from LLM", "red"))
        return {
            "graph_number": graph_num,
            "graph_edges": edges,
            "graph_string": graph_str,
            "start_node": start_node,
            "end_node": end_node,
            "correct_distance": correct_distance,
            "correct_path": correct_path,
            "llm_response": None,
            "llm_distance": None,
            "llm_path": [],
            "is_correct": False,
            "visualization_file": viz_filename
        }

def analyze_results(results):
    """Analyze the results and provide statistics"""
    total_graphs = len(results)
    correct_answers = sum(1 for result in results if result["is_correct"])
    accuracy = (correct_answers / total_graphs) * 100 if total_graphs > 0 else 0

    print(colored(f"\n{'='*60}", "cyan"))
    print(colored("GRAPH THEORY ANALYSIS RESULTS", "cyan"))
    print(colored(f"{'='*60}", "cyan"))
    print(colored(f"Total Graphs: {total_graphs}", "yellow"))
    print(colored(f"Correct Solutions: {correct_answers}", "green"))
    print(colored(f"Accuracy: {accuracy:.1f}%", "blue"))

    if correct_answers < total_graphs:
        print(colored("\nINCORRECT SOLUTIONS:", "red"))
        for result in results:
            if not result["is_correct"]:
                print(colored(f"G{result['graph_number']}: Start {result['start_node']} -> End {result['end_node']}", "red"))

def save_to_json(results, filename="graph_results.json"):
    """Save results to JSON file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"graph_results_{timestamp}.json"

    # Create summary stats
    total = len(results)
    correct = sum(1 for r in results if r["is_correct"])
    accuracy = (correct / total) * 100 if total > 0 else 0

    data = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "total_graphs": total,
            "correct_answers": correct,
            "accuracy": round(accuracy, 2),
            "model": MODEL_NAME,
            "num_nodes": NUM_NODES,
            "max_weight": MAX_WEIGHT
        },
        "results": results
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(colored(f"\nResults saved to: {filename}", "green"))
    return filename

async def main():
    """Main function to run graph theory shortest path testing"""
    print(colored("Setting up OpenRouter client...", "green"))
    print(colored(f"Generating random graphs with {NUM_NODES} nodes...", "green"))

    # Check if API key is set
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "<OPENROUTER_API_KEY>":
        print(colored("ERROR: Please set your OPENROUTER_API_KEY environment variable!", "red"))
        return

    client = setup_openai_client()

    print(colored(f"\nGenerating {NUM_GRAPHS} random graphs...", "green"))

    # Generate all graphs first
    graphs_data = []
    for i in range(NUM_GRAPHS):
        adj_list, graph_str, start_node, end_node, edges = generate_random_graph()
        graphs_data.append((i+1, adj_list, graph_str, start_node, end_node, edges))

    print(colored(f"\nAsking LLM to solve {NUM_GRAPHS} shortest path problems in parallel...", "green"))
    print(colored("="*80, "cyan"))

    # Create async tasks for all graphs
    tasks = [
        process_single_graph(client, graph_num, adj_list, graph_str, start_node, end_node, edges)
        for graph_num, adj_list, graph_str, start_node, end_node, edges in graphs_data
    ]

    # Run all shortest path computations in parallel
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle any exceptions
    final_results = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(colored(f"Error in graph {i+1}: {result}", "red"))
            graph_num, adj_list, graph_str, start_node, end_node, edges = graphs_data[i]
            correct_distance, correct_path = dijkstra_shortest_path(adj_list, start_node, end_node)
            final_results.append({
                "graph_number": graph_num,
                "graph_edges": edges,
                "graph_string": graph_str,
                "start_node": start_node,
                "end_node": end_node,
                "correct_distance": correct_distance,
                "correct_path": correct_path,
                "llm_response": f"Error: {str(result)}",
                "llm_distance": None,
                "llm_path": [],
                "is_correct": False
            })
        else:
            final_results.append(result)

    print(colored("\n" + "="*60, "cyan"))

    # Analyze and display results
    analyze_results(final_results)

    # Save results to JSON
    json_filename = save_to_json(final_results)

    print(colored(f"\nSummary: {len(final_results)} graphs processed", "yellow"))
    print(colored(f"JSON results saved to: {json_filename}", "green"))

if __name__ == "__main__":
    asyncio.run(main())
