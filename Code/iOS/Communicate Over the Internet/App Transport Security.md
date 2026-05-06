

Enabling unencrypted HTTP in your iOS app.

---

## Steps

1. Open `Info.plist`
2. Right click on the empty space
3. Select "Add Row"
4. Select "App Transport Security Settings"
5. Add an attribute with the plus icon
6. Set "Allow Arbitrary Loads" to **YES**

---

## Note

This allows your app to make HTTP requests to servers that don't use HTTPS encryption. Use with caution in production environments.