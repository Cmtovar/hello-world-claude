# Debug Steps for Preview Issue

## Step 1: Open Console
1. Open page: `http://100.93.126.24:8080/`
2. Press **F12** (or right-click → Inspect → Console tab)
3. Keep console open

## Step 2: Click Test Card
1. Click "Descend 1 Block" card
2. Watch console output

## Expected Console Output

You should see something like:
```
Initializing preview scene for: Descend 1 Block
Canvas: <canvas id="previewCanvas">
Container: <div id="previewContent">
Container size: 480 x 350
Preview renderer created: WebGLRenderer {...}
Lights added. Scene children: 2
Updating preview scene for mechanic: {name: "Descend 1 Block", ...}
Loading test map: testDescendOneBlock
Test config loaded: {name: "Test Descend One Block", ...}
Creating 6 voxels
Voxels added. Scene now has 8 children
Creating player at {x: 0, y: 2, z: 0}
Player added at position: Vector3 {x: 0, y: 2.6, z: 0}
Preview animation loop started
```

## What to Check

### Problem 1: No console output at all
**Issue:** JavaScript error before preview opens
**Check:** Look for red errors in console

### Problem 2: "Container size: 0 x 0"
**Issue:** Container hasn't laid out yet
**This is the likely problem!**

### Problem 3: "Failed to load test map"
**Issue:** Test map JSON not found
**Check:** Network tab, look for 404 error

### Problem 4: Scene children stays at 2
**Issue:** Voxels not being added
**Means JSON loaded but forEach failed**

## Report Back

Tell me:
1. What console output you see
2. Any red errors?
3. What is "Container size: X x Y"?
4. Does "Scene now has X children" show a number > 2?

This will tell me exactly what's broken.
