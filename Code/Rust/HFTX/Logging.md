- Add `Debug` derives to structs for `{:#?}` dumps
    
- Lightweight logging (pick one):
    
    - `eprintln!()` during dev
        
    - `log` + `env_logger` with levels: `trace!`, `debug!`, `info!`
        
- Pretty-print ladders for snapshots in tests