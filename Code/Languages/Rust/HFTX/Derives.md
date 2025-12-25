- Implements traits for your type

| Derivation  | Implementation                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| `Clone`     | make explicit duplicates with `.clone()`<br>Allows owned data to be a new independent copy                |
| `Copy`      | enables implicit, bit-for-bit copying on move<br>For simple, non-heap types.                              |
| `Debug`     | enables `{:?}` formatting (`println!("{:?}", val)` helpful for tests and logs)                            |
| `PartialEq` | Allows for `==` / `!=` comparisons                                                                        |
| `Eq`        | Marker trait meaning equality is total (no NaN-like weird cases)<br>Usually derived alongside `PartialEq` |
| `Hash`      | Allows to use `HashMap `/ `HashSet`                                                                       |

---
