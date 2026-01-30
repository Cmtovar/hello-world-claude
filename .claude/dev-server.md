# Development Server Configuration

## Tailscale IP Preference

**Always host the development server on the tailscale IP address, not localhost.**

**Tailscale IP:** `100.93.126.24`

### Command
```bash
python -m http.server -b 100.93.126.24 8080
```

### URL Format
```
http://100.93.126.24:8080/
```

### Loading Test Maps
```
http://100.93.126.24:8080/?test=complete-scene
http://100.93.126.24:8080/?test=ruins-test
http://100.93.126.24:8080/?test=bridge-test
```

### Why Tailscale IP?
- Accessible across devices on tailscale network
- Consistent IP for development
- Allows testing on multiple devices simultaneously

---

**Created:** 2026-01-30
**Persistent preference** - Always use this IP for hosting during development
