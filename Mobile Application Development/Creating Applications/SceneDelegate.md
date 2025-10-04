**Concept**  
- Handles lifecycle of **UI windows (scenes)**.  
- Runs when app supports multiple windows or enters background/foreground.  

**Common Methods**
- `scene(_:willConnectTo:options:)` → configure new window.  
- `sceneDidEnterBackground(_:)` → save UI state.  
- `sceneWillEnterForeground(_:)` → prepare UI for display.  

**Related**  
- [[AppDelegate]]  
- [[ViewController]]