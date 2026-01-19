---
layout: doc
---

# Apps & Platforms City 🏙️

![React](https://img.shields.io/badge/React-19.0-blue?logo=react)
![Three.js](https://img.shields.io/badge/Three.js-0.182-black?logo=three.js)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.0-38bdf8?logo=tailwindcss)
![Vite](https://img.shields.io/badge/Vite-7.0-646cff?logo=vite)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

**Apps & Platforms City** is an immersive 3D web experience that reimagines the traditional "Link in Bio" or dashboard. Instead of a list of static links, users explore a vibrant, interactive city where every building represents a major social media, learning, or productivity platform.

Built with **React 19** and **Three.js**, this application demonstrates how to combine standard web technologies with 3D graphics to create gamified user interfaces.

---

## Features

- **Interactive 3D World**: A fully explorable city built with Three.js, featuring dynamic lighting, distinct building architectures, and textured environments.
- **Cross-Platform Controls**:
  - **Desktop**: FPS-style movement (WASD/Arrows) and mouse look.
  - **Mobile**: Touch-optimized controls with on-screen D-pad and interaction buttons.
- **Proximity Interactions**: Smart detection systems trigger UI prompts when the user approaches specific buildings.
- **Rich Platform Ecosystem**: Dedicated hubs for over 20+ platforms including Reddit, GitHub, YouTube, LinkedIn, and more.
- **Modern Tech Stack**: severe performance optimizations using Vite and Tailwind CSS v4.
- **Docker Ready**: Includes a multi-stage Dockerfile for production-grade containerization with Nginx.

## Tech Stack

- **Core Framework**: [React 19](https://react.dev/)
- **3D Engine**: [Three.js](https://threejs.org/) (Vanilla Three.js logic integrated via React hooks)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **Build Tool**: [Vite 7](https://vitejs.dev/)
- **Routing**: [React Router v7](https://reactrouter.com/)
- **Linting**: ESLint (v9)

## Project Structure

The project follows a component-driven architecture:

```
apps-platforms-city/
├── public/                 # Static assets (textures, platform logos)
├── src/
│   ├── assets/             # Internal assets
│   ├── components/
│   │   ├── City.jsx        # 🧠 Core 3D Engine (Scene, Camera, Player Logic)
│   │   ├── WelcomePage.jsx # Landing screen
│   │   ├── Behance.jsx     
│   │   ├── Chatgbt.jsx
│   │   ├── City.jsx
│   │   ├── Discord.jsx
│   │   ├── Freecodecamp.jsx
│   │   ├── Gemini.jsx
│   │   ├── GitHub.jsx
│   │   ├── Google.jsx
│   │   ├── Instagram.jsx
│   │   ├── KhanAcademy.jsx
│   │   ├── LinkedIn.jsx
│   │   ├── Notion.jsx
│   │   ├── Reddit.jsx
│   │   ├── Shark Tank.jsx
│   │   ├── Stackoverflow.jsx
│   │   ├── Udemy.jsx
│   │   ├── Youtube.jsx
│   ├── CSS/
│   │   └── City.css        # Specific styles for the 3D canvas and overlay UI
│   ├── App.jsx             # Main Routing setup
│   └── main.jsx            # Application Entry point
├── Dockerfile              # Multi-stage Docker build config
├── vercel.json             # Vercel deployment configuration
├── vite.config.js          # Vite configuration with Tailwind integration
└── package.json            # Dependencies and scripts
```

## Getting Started

### Prerequisites
- **Node.js**: v18 or higher
- **npm**: v9 or higher

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/apps-platforms-city.git
   cd apps-platforms-city
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```
   Access the app at `http://localhost:5173`.

### Production Build

To create an optimized production build:

```bash
npm run build
```
The output will be in the `dist/` directory. You can preview it locally using:
```bash
npm run preview
```

## Docker Deployment

This project includes a production-ready `Dockerfile` serving the app via Nginx.

1. **Build the Docker image**
   ```bash
   docker build -t apps-platforms-city .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:80 apps-platforms-city
   ```
   Access the app at `http://localhost:8080`.

## Controls

| Action | Desktop (Keyboard) | Mobile (Touch Interface) |
| :--- | :--- | :--- |
| **Move Forward** | `W` or `Arrow Up` | `▲` Button |
| **Move Backward** | `S` or `Arrow Down` | `▼` Button |
| **Turn Left** | `A` or `Arrow Left` | `◄` Button |
| **Turn Right** | `D` or `Arrow Right` | `►` Button |
| **Enter Building** | Click "Visit [Platform]" | Tap "Visit [Platform]" |

## Platforms & Zones

The city is organized into thematic zones:

- **Social Media**: Reddit, Instagram, Discord, Pinterest, Shark Tank
- **Tech & Dev**: GitHub, Stack Overflow, FreeCodeCamp
- **Education**: Udemy, Coursera, Khan Academy
- **Productivity**: Notion, Google Workspace, LinkedIn
- **Artificial Intelligence**: ChatGPT, Gemini
- **Creative & Media**: Behance, YouTube

## Contributing

We welcome contributions to expand the city!

1. **Fork** the repository.
2. **Create a branch** for your feature: `git checkout -b feature/NewBuilding`.
3. **Commit** your changes: `git commit -m 'Add Twitter building'`.
4. **Push** to the branch: `git push origin feature/NewBuilding`.
5. Open a **Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
