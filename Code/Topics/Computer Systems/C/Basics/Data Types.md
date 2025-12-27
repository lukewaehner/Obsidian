

C provides several built-in data types for storing different kinds of information.

## Primitive Types

### Integral Types (Signed and Unsigned)

For unsigned types, use `unsigned` keyword (e.g., `unsigned short int`)

| Type      | Size           | Description |
| --------- | -------------- | ----------- |
| char      | 1 byte (8-bit) | Single character or small integer |
| short int | 16-bit         | Short integer |
| int       | 32-bit         | Standard integer |
| long int  | 64-bit         | Long integer |

### Floating-Point Types

| Type   | Size   | Description |
| ------ | ------ | ----------- |
| float  | 32-bit | Single precision decimal |
| double | 64-bit | Double precision decimal |

## Composite Types

### Structs
User-defined types that group related data together.

### Union
Similar to struct but members share the same memory location.

## Usage Examples

```c
char letter = 'A';
int number = 42;
float pi = 3.14f;
double precise_pi = 3.141592653589793;
unsigned int positive_only = 100;
```

## Related Topics
- [[Code/Topics/Computer Systems/C/Basics/Functions]]
- [[Code/Topics/Computer Systems/C/Basics/Arrays]]
- [[Hello World Program]]