# Math Animations: Understanding Trigonometric Art

This collection demonstrates how simple mathematical concepts create beautiful, organic animations using p5.js.

## 🎯 Core Concepts

### 1. Sin & Cos: Circles vs Waves

**In Math Class (Waves):**
```javascript
y = sin(x)  // Creates a wave along x-axis
y = cos(x)  // Creates another wave along x-axis
```

**For Animations (Circles):**
```javascript
x = cos(angle)  // Horizontal position
y = sin(angle)  // Vertical position
// Together they create a perfect circle!
```

### 2. Time-Based Animation

```javascript
let time = 0;

function draw() {
  time += 0.02;  // Increases every frame

  // Use time in trigonometric functions for movement
  x = radius * cos(time);     // Rotation
  x = radius * cos(time/2);   // Slower rotation
  x = radius * cos(2*time);   // Faster rotation
}
```

### 3. Loops Creating Shapes

Animations use loops to draw thousands of points:

```javascript
for (let i = 0; i < 10000; i++) {
  // Calculate position for each point
  let x = someFormula(i, time);
  let y = anotherFormula(i, time);
  point(x, y);  // Draw one point
}
// Result: Complex shape from many individual points!
```

## 📁 Files in This Collection

### `original_math_animation.html`
The complex, swirling pattern that started it all. Uses 10,000 points with layered trigonometric calculations.

**Key Formula:**
```javascript
const x = q + 90*Math.cos(c) + 200;
const y = q*Math.sin(c) + 29*d - 170;
```

### `simple_rotation_demo.html`
Basic demonstration of sin/cos creating circles with time-based rotation.

**Shows:**
- How `cos(time)` and `sin(time)` create circular motion
- Different rotation speeds: `time`, `time/2`, `2*time`, `-time`
- Circle center positioning

### `enhanced_rotation_demo.html`
Adds visual elements to understand the math better.

**Features:**
- Circle outlines showing paths
- Connecting lines from center to points
- Time indicator
- Semi-transparent elements

### `loop_shapes_demo.html`
Demonstrates how loops create complex shapes from simple math.

**Examples:**
1. **Spiral**: `angle = i * 0.1`, `radius = i * 0.5`
2. **Flower**: Nested loops (petals × points per petal)
3. **Starburst**: Rays with wavy motion

## 🔧 p5.js Special Functions

p5.js automatically calls these functions:

```javascript
function setup()        // Runs once at start
function draw()         // Runs every frame (~60x/sec)
function mousePressed() // When mouse clicked
function keyPressed()   // When key pressed
function windowResized() // When window resized
```

## 📐 Mathematical Building Blocks

### Time Variable
```javascript
let time = 0;
time += 0.02;  // Controls animation speed
```

### Basic Circle
```javascript
let radius = 100;
let x = radius * cos(time) + centerX;
let y = radius * sin(time) + centerY;
```

### Position Offsets
```javascript
+ 200  // Moves circle center to (200, 200) on 400×400 canvas
```

### Speed Variations
```javascript
cos(time)     // Normal speed
cos(time/2)   // Half speed (slower)
cos(2*time)   // Double speed (faster)
cos(-time)    // Reverse direction
```

## 🎨 How the Original Animation Works

The original uses these principles:

1. **Loop 10,000 times** - each iteration draws one point
2. **Complex nested calculations** - multiple sin/cos with different time multipliers
3. **Conditional logic** - different behavior for different ranges
4. **Distance calculations** - `Math.hypot()` for organic shapes

**Result:** What looks like random art is actually thousands of points, each positioned by precise mathematical formulas that evolve over time.

## 🚀 Running the Animations

Simply open any `.html` file in a web browser. No server required - p5.js loads from CDN.

## 🎓 Learning Progression

1. **Start with `simple_rotation_demo.html`** - Basic sin/cos circles
2. **Try `enhanced_rotation_demo.html`** - Visual guides added
3. **Explore `loop_shapes_demo.html`** - How loops build shapes
4. **Study `original_math_animation.html`** - The complex result

## 💡 Key Insights

- **Sin/Cos + Time = Rotation**
- **Loops + Math = Complex Shapes**
- **Many Points = Organic Patterns**
- **Different Speeds = Evolution**

The beauty emerges from simple math repeated thousands of times with slight variations in timing and positioning!
