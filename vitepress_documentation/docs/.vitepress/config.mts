import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Apps-Platforms-City",
  description: "Documentation for Apps-Platforms-City",
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' }
    ],
    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Introduction', link: '/' }
        ]
      }
    ],
    socialLinks: [
    ]
  }
})
