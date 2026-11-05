# 🎬 NullSound Studio Pro

> **AI & Cinematic Hollywood Sound Effects Suite**  
> Complete reverse-engineered audio suite inspired by viral cinematic storytelling (*Null Hour* / Hans Zimmer style).

🔗 **Live Deployment on Vercel:** [https://nullsound-studio.vercel.app](https://nullsound-studio.vercel.app)

---

## 🌟 Highlights & Features

- **47 Master Audio Assets**:
  - **Full 21-Minute Movie Track**: Direct master audio from the viral 9.6M-view hit (*xRQG07hiLr0*).
  - **8 Exact Scene Slices**: Sliced losslessly from the movie (Dragon reveal roars, tree destruction, girl pursuit chase, swamp ambush, monkey theft, temple ruins heartbeat, and rainforest rain).
  - **38 Hollywood Studio Master Recordings**: Full-length (>10s to 170s) acoustic foley and sound effects with zero short synthetic beeps.
- **Interactive Audio Engine**:
  - Real-time seekable scrubber progress bar.
  - Animated multi-frequency audio visualizer.
  - 1-click Download buttons (M4A & MP3) formatted for instant CapCut timeline dropping.
  - Multi-category filter tabs (Dragon Roars, Crashes & Impacts, Chase Foley, Swamp, Jungle Atmospheres, Suspense & Braams).
- **Production Ready**:
  - Deployed directly to Vercel edge network with CORS streaming and byte-range request support.

---

## 📂 Project Structure

```
NullSound_Studio/
├── index.html            # Complete responsive web application
├── vercel.json           # Vercel deployment configuration & CORS headers
├── .vercelignore         # Deployment exclusions
├── run_nullsound.py      # Local Python HTTP streaming server with CORS
└── audio/                # 47 High-Fidelity Audio Tracks (M4A & MP3)
    ├── nullhour_original_movie_audio.m4a (21m 54s)
    ├── nh_movie_*.m4a (8 movie scene cuts)
    └── *.mp3 (38 Hollywood studio master tracks)
```

---

## 🚀 Running Locally

1. Clone or download this repository.
2. Run the local streaming server:
   ```bash
   python run_nullsound.py
   ```
3. Open your browser at:
   ```
   http://localhost:7860
   ```

---

## 🛠 CapCut 3-Track Timeline Setup

1. **Track 1 (Ambience at -14dB)**: `Tropical Rainforest Heavy Rain` (99s) or `Null Hour Jungle Entry`.
2. **Track 2 (Music at -18dB)**: `Null Hour Official Movie Background Music` or `Dark Horror Ambience Score`.
3. **Track 3 (Spot SFX at -3dB to 0dB)**: Drop dragon roars, tree crashes, and panicked mud sprint footsteps exactly when action happens on screen.

---

## 📜 License
MIT License
