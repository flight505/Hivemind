import openai
import os
from termcolor import colored

#

# Check if conversation_id.txt exists and has content
conversation_id_file = "conversation_id.txt"

try:
    if os.path.exists(conversation_id_file) and os.path.getsize(conversation_id_file) > 0:
        # Read existing conversation ID
        with open(conversation_id_file, "r") as f:
            conversation_id = f.read().strip()
        print(colored(f"📋 Using existing conversation ID: {conversation_id}", "cyan"))
    else:
        # Create new conversation
        print(colored("🔄 Creating new conversation...", "yellow"))
        conversation = openai.conversations.create()
        conversation_id = conversation.id

        # Save conversation ID to file
        with open(conversation_id_file, "w") as f:
            f.write(conversation_id)

        print(colored(f"✨ Created new conversation with ID: {conversation_id}", "green"))
        print(colored(f"💾 Conversation ID saved to {conversation_id_file}", "cyan"))
except Exception as e:
    print(colored(f"❌ Error managing conversation ID: {str(e)}", "red"))
    # Fallback: create a temporary conversation ID
    print(colored("🔄 Creating temporary conversation...", "yellow"))
    conversation = openai.conversations.create()
    conversation_id = conversation.id
    print(colored(f"⚠️ Using temporary conversation ID: {conversation_id}", "yellow"))

print(colored("\n🎉 Welcome to AI Chat! Type 'exit' or 'quit' to end the conversation.\n", "yellow", attrs=["bold"]))

# Continuous chat loop
while True:
    # Get user input
    user_message = input(colored("👤 You: ", "blue", attrs=["bold"])).strip()

    if user_message.lower() in ['exit', 'quit', 'bye']:
        print(colored("\n👋 Goodbye! Thanks for chatting!", "red", attrs=["bold"]))
        break

    if not user_message:
        print(colored("⚠️  Please enter a message.", "yellow"))
        continue

    try:
        # Send message to AI
        response = openai.responses.create(
            model="gpt-4.1",
            input=[{"role": "user", "content": user_message}],
            conversation=conversation_id,
            tools=[
                {
                    "type": "code_interpreter",
                    "container": {"type": "auto"}
                }
            ],
            include=["code_interpreter_call.outputs"]
        )

        # Display AI response
        print(colored(f"🤖 AI: {response.output_text}", "green"))

        # Display token usage info
        if hasattr(response, 'usage') and response.usage:
            print(colored(f"📊 Token Usage: {response.usage}", "magenta"))

        print()  # Add spacing

    except Exception as e:
        print(colored(f"❌ Error: {str(e)}", "red"))
        print()
