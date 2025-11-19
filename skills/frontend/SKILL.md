---
name: frontend-development
description: Master frontend frameworks (React, Vue, Angular), styling, state management, and web performance. Use when building web applications, designing user interfaces, or learning frontend technologies.
---

# Frontend Development

## Quick Start

Frontend development involves building user interfaces for web applications. The roadmap covers:

### Core Technologies
- **HTML & CSS**: Structure and styling fundamentals
- **JavaScript**: Core language (ES6+, async/await, modules)
- **Frameworks**: React, Vue, Angular, Svelte
- **Styling**: Tailwind CSS, Sass, PostCSS
- **State Management**: Context, Zustand, Jotai, Redux, Pinia
- **Routing**: React Router, Vue Router, Angular Routing
- **Testing**: Jest, Cypress, Playwright, Vitest

### Learning Resources
1. Start with HTML, CSS, JavaScript fundamentals
2. Choose a framework: React (most popular), Vue (approachable), Angular (enterprise)
3. Learn state management for your chosen framework
4. Master testing frameworks and tools
5. Practice building complete applications

### Key Frameworks Overview

**React**: Component-based, hooks for state management, huge ecosystem
```javascript
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

**Vue**: Progressive framework, single-file components, gentle learning curve
```vue
<template>
  <button @click="count++">Count: {{ count }}</button>
</template>

<script>
export default {
  data() {
    return { count: 0 }
  }
}
</script>
```

**Angular**: Full framework, TypeScript-first, enterprise-ready
```typescript
@Component({
  selector: 'app-counter',
  template: '<button (click)="increment()">Count: {{ count }}</button>'
})
export class CounterComponent {
  count = 0;
  increment() { this.count++; }
}
```

## Study Path

1. **Foundations** (1-2 weeks): HTML, CSS, JavaScript basics
2. **Framework Choice** (2-3 weeks): Pick React, Vue, or Angular
3. **Advanced Concepts** (4-6 weeks): Hooks, composition, state management
4. **Ecosystem Tools** (2-3 weeks): Build tools, testing, routing
5. **Real Projects** (ongoing): Build complete applications

## Common Challenges
- Choosing the right framework for your needs
- Managing application state effectively
- Optimizing performance and bundle size
- Testing components and integrations
- Learning the ecosystem around your framework

## Resources
- Developer Roadmap: https://roadmap.sh/frontend
- React: https://react.dev
- Vue: https://vuejs.org
- Angular: https://angular.io
