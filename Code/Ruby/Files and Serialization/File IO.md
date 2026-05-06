---
tags:
  - ruby
type: note
related:
  - '[[Files and Serialization]]'
  - '[[Serialization]]'
  - '[[JSON in Ruby]]'
  - '[[YAML in Ruby]]'
  - '[[Ruby]]'
---
# File IO

Reading from and writing to files on the hard drive.

## Overview

Files are streams of bytes that Ruby reads from top to bottom. Ruby's `File` class (which inherits from `IO`) provides simple methods to read entire files into strings or arrays, write data out, and perform more advanced operations like reading line-by-line or seeking to specific positions.

## Reading Files

### Read Entire File

```ruby
# Read entire file as a single string
content = File.read('data.txt')
# => "line one\nline two\nline three\n"

# Read as array of lines (includes newlines)
lines = File.readlines('data.txt')
# => ["line one\n", "line two\n", "line three\n"]

# Read as array, stripping newlines
lines = File.readlines('data.txt', chomp: true)
# => ["line one", "line two", "line three"]
```

### Read with Block (Memory Efficient)

For large files, process line-by-line instead of loading everything:

```ruby
File.foreach('large_file.txt') do |line|
  puts line.upcase
end

# Or with each_line
File.open('data.txt') do |file|
  file.each_line { |line| puts line }
end
```

### Manual Open/Close

```ruby
file = File.open('data.txt', 'r')  # 'r' = read mode (default)
content = file.read
file.close  # Don't forget to close!

# Better: block form auto-closes
File.open('data.txt', 'r') do |file|
  content = file.read
end  # Automatically closed here
```

## Writing Files

### Write Entire File

```ruby
# Overwrites existing file or creates new one
File.write('output.txt', 'Hello, World!')

# Append to existing file
File.write('output.txt', 'More content', mode: 'a')

# Write array of lines
lines = ['line 1', 'line 2', 'line 3']
File.write('output.txt', lines.join("\n"))
```

### Write with Block

```ruby
File.open('output.txt', 'w') do |file|  # 'w' = write mode
  file.puts 'First line'
  file.puts 'Second line'
  file.print 'No newline here'
  file.write 'Also no newline'
end
```

### Append Mode

```ruby
File.open('log.txt', 'a') do |file|  # 'a' = append mode
  file.puts "[#{Time.now}] Event occurred"
end
```

## File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read only (default), starts at beginning |
| `'w'` | Write only, truncates existing file |
| `'a'` | Append, write only, starts at end |
| `'r+'` | Read and write, starts at beginning |
| `'w+'` | Read and write, truncates file |
| `'a+'` | Read and append, starts at end |

Add `b` for binary mode: `'rb'`, `'wb'`, etc.

## File Position

Files track a current position (cursor) as you read/write:

```ruby
File.open('data.txt', 'r') do |file|
  file.read(5)       # Read 5 bytes
  file.pos           # => 5 (current position)
  
  file.gets          # Read until newline
  file.pos           # => position after that line
  
  file.rewind        # Back to beginning
  file.pos           # => 0
  
  file.seek(10)      # Jump to byte 10
  file.pos           # => 10
  
  file.eof?          # => false (not at end of file)
end
```

## The IO Class

`File` inherits from `IO`, Ruby's base class for input/output streams:

```ruby
# Standard streams are IO objects
STDIN   # Standard input (keyboard)
STDOUT  # Standard output (console)
STDERR  # Standard error

# Global aliases (can be reassigned)
$stdin   # => STDIN by default
$stdout  # => STDOUT by default
$stderr  # => STDERR by default

# Low-level IO (file descriptors)
io = IO.new(1)  # fd 1 = stdout
io.puts 'Hello' # => prints to console
```

### File Descriptors

Every open file has a numeric descriptor:
- `0` — Standard input (`/dev/fd/0`)
- `1` — Standard output (`/dev/fd/1`)
- `2` — Standard error (`/dev/fd/2`)
- `3+` — Other opened files

```ruby
fd = IO.sysopen('data.txt', 'r')  # Returns file descriptor
# => 8

file = IO.new(fd)
file.gets  # Read a line
file.close
```

## File Information

```ruby
# Check existence
File.exist?('data.txt')      # => true/false
File.file?('data.txt')       # => true if it's a file
File.directory?('folder')    # => true if it's a directory

# File stats
File.size('data.txt')        # => size in bytes
File.mtime('data.txt')       # => last modified time
File.readable?('data.txt')   # => true if readable
File.writable?('data.txt')   # => true if writable

# Path manipulation
File.basename('/path/to/file.txt')      # => "file.txt"
File.dirname('/path/to/file.txt')       # => "/path/to"
File.extname('/path/to/file.txt')       # => ".txt"
File.expand_path('~/documents')         # => "/home/user/documents"
File.join('path', 'to', 'file.txt')     # => "path/to/file.txt"
```

## Directory Operations

```ruby
# Current directory
Dir.pwd                      # => "/home/user/project"

# Change directory
Dir.chdir('/tmp') do
  # Inside /tmp here
end  # Back to original directory

# List files
Dir.entries('.')             # => [".", "..", "file1.rb", ...]
Dir.glob('*.rb')             # => ["file1.rb", "file2.rb"]
Dir.glob('**/*.rb')          # => Recursive search

# Create/delete directories
Dir.mkdir('new_folder')
Dir.rmdir('empty_folder')    # Must be empty

# Check if directory
Dir.exist?('folder')         # => true/false
```

## Common Patterns

### Safe File Reading

```ruby
def read_file(path)
  return nil unless File.exist?(path)
  File.read(path)
rescue IOError, SystemCallError => e
  puts "Error reading file: #{e.message}"
  nil
end
```

### Processing Large Files

```ruby
# Don't do this for large files:
# content = File.read('huge.txt')  # Loads entire file into memory

# Do this instead:
File.foreach('huge.txt') do |line|
  process(line)
end

# Or use lazy enumeration
File.open('huge.txt').each_line.lazy
  .map(&:chomp)
  .select { |line| line.include?('error') }
  .first(10)
```

### Temporary Files

```ruby
require 'tempfile'

Tempfile.create('prefix') do |file|
  file.write('temporary data')
  file.rewind
  file.read  # => "temporary data"
end  # File automatically deleted
```

### Reading Binary Files

```ruby
# Images, PDFs, etc.
binary_data = File.binread('image.png')

# Or with mode
File.open('image.png', 'rb') do |file|
  binary_data = file.read
end

# Writing binary
File.binwrite('copy.png', binary_data)
```

## Tips

- Always use block form (`File.open { }`) to ensure files are closed
- Use `File.read`/`File.write` for simple one-shot operations
- Process large files line-by-line with `File.foreach`
- Use `File.join` for cross-platform path building
- Remember: files are read top-to-bottom as streams of bytes
- Check `File.exist?` before reading to avoid errors
- Use `'rb'`/`'wb'` modes for binary files (images, etc.)

## See Also

- [[Files and Serialization]]
- [[Serialization]] — Converting objects to strings for storage
- [[JSON in Ruby]] — Reading/writing JSON files
- [[YAML in Ruby]] — Reading/writing YAML files
- [[Input Output]] — Console I/O
- [[Ruby]]
