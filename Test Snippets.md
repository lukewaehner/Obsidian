```python
print("Running Python from Obsidian!")
print("=" * 40)
for i in range(5):
    print(f"Count: {i}")
```


```python
import sys
name = sys.argv[1] if len(sys.argv) > 1 else "World"
age = sys.argv[2] if len(sys.argv) > 2 else "unknown"
print(f"Hello {name}!")
print(f"Age: {age}")
```


```python
print("This causes an error!
```


```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "C++ in Obsidian!" << endl;
    for(int i = 0; i < 3; i++) {
        cout << "Iteration " << i << endl;
    }
    return 0;
}
```


```ruby
puts "Ruby in Obsidian!"
puts "=" * 30
fruits = ["apple", "banana", "cherry"]
fruits.each_with_index do |fruit, i|
  puts "#{i + 1}. #{fruit}"
end
```


```rust
fn main() {
	println!("Can add in path specific executions too");
}
```
