

**Concept**  
- Manages **application lifecycle**.  
- Entry point when the app launches.  

**Common Methods**
- `application(_:didFinishLaunchingWithOptions:)` → setup code on launch.  
- `applicationDidEnterBackground(_:)` → pause tasks, save state.  
- `applicationWillEnterForeground(_:)` → resume tasks.  

**Related**  
- [[SceneDelegate]]