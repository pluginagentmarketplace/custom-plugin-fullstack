---
name: recommend
description: Get Role Recommendations
allowed-tools: Read
---

# /recommend - Get Role Recommendations

Get personalized role recommendations based on your skills, interests, and career goals.

## Usage

```
/recommend
/recommend [criteria]
```

## Examples

- `/recommend` - Get general recommendations
- `/recommend skilled-at:javascript` - Based on JavaScript skills
- `/recommend interests:web,startups` - Web development in startups
- `/recommend level:senior` - Senior-level roles
- `/recommend salary:high` - High-paying roles

## How It Works

The recommendation engine considers:

### 1. Your Skills
- Current technical skills
- Proficiency levels
- Learning speed
- Growth areas

### 2. Your Interests
- Technologies you like
- Problem domains
- Work environment
- Team dynamics

### 3. Your Goals
- Career progression
- Salary expectations
- Work-life balance
- Learning opportunities
- Impact and meaning

### 4. Market Factors
- Job availability
- Salary ranges
- Growth trends
- Remote opportunities

## Recommendation Categories

### By Career Stage

**Beginner (0-2 years)**
- Frontend Developer
- Backend Developer
- Mobile Developer

**Intermediate (2-5 years)**
- Full-stack Developer
- Senior Frontend Developer
- Backend Specialist

**Advanced (5+ years)**
- Lead Engineer
- Tech Lead
- Engineering Manager
- Architect

### By Interest Area

**Web Technologies**
→ Frontend Developer, Full-stack Developer, React/Vue/Angular Expert

**Mobile Development**
→ React Native Developer, Flutter Developer, iOS/Android Native

**Cloud & Infrastructure**
→ DevOps Engineer, Cloud Architect, Infrastructure Engineer

**Data & AI**
→ Data Engineer, Machine Learning Engineer, Data Scientist

**Security**
→ Security Engineer, Cybersecurity Expert, Penetration Tester

**Leadership**
→ Engineering Manager, Tech Lead, Architect, VP Engineering

### By Work Style

**Independent Contributors**
- Senior Developer
- Architect
- Specialist Engineer

**Team Leaders**
- Tech Lead
- Engineering Manager
- Scrum Master

**Full Involvement**
- Product Manager
- Designer
- QA Engineer

## Recommendation Output

### 1. Top 3 Matches
```
Match #1: React Developer ⭐⭐⭐⭐⭐ 95% match
├─ Salary: $120K-180K
├─ Job Growth: High 📈
├─ Remote-Friendly: Yes ✓
└─ Why: JavaScript skills + web interest

Match #2: Full-stack Developer ⭐⭐⭐⭐ 88% match
├─ Salary: $130K-190K
├─ Job Growth: Very High 📈
├─ Remote-Friendly: Yes ✓
└─ Why: JavaScript + Backend interest

Match #3: Backend Developer ⭐⭐⭐⭐ 82% match
├─ Salary: $110K-170K
├─ Job Growth: High 📈
├─ Remote-Friendly: Yes ✓
└─ Why: Database + API design interest
```

### 2. Skills to Develop
For each recommended role, you'll get:
- Skills you already have
- Skills you need to develop
- Learning timeline
- Resource recommendations

### 3. Alternative Paths
```
Quick Path (6 months)
→ React Developer → Full-stack Developer

Thorough Path (12 months)
→ Frontend → JavaScript Mastery → Full-stack → Backend

Advanced Path (18+ months)
→ Frontend → Full-stack → System Design → Architect
```

### 4. Next Steps
1. Take `/assess` to validate the fit
2. Start `/learn [recommended-role]`
3. Build projects in the recommended area
4. Join communities for the role
5. Network with professionals in the field

## Customization

### Adjust by Preferences
```
/recommend
   --level intermediate
   --interests web,startups
   --work-style remote-first
   --salary-target 150000
   --growth-priority high
```

### Refine Results
After initial recommendation:
- `/recommend more-like:react-developer`
- `/recommend different-from:mobile`
- `/recommend leadership-track`
- `/recommend ic-track` (Individual Contributor)

## Special Recommendations

### Career Pivots
If you want to change careers:
- We show which roles build on your current skills
- We highlight transferable skills
- We recommend learning paths optimized for transitions

### Parallel Tracks
Some recommendations include parallel learning:
```
Month 1-3: Core skill (Backend fundamentals)
Month 3-6: Primary track (Node.js) + Secondary track (DevOps basics)
Month 6-12: Specialization (Full-stack or Lead Engineer)
```

### Accelerated Paths
For fast learners with relevant background:
- Compressed timelines
- Advanced projects
- Mentorship opportunities
- Certification recommendations

## Tips

1. **Be Specific**: More details = better recommendations
2. **Consider Growth**: Choose based on learning, not just salary
3. **Follow the Path**: Recommended roles are designed to build on each other
4. **Take Action**: Use `/learn` to start the recommended path
5. **Revisit**: Reassess every 6-12 months

## Integration with Other Commands

```
/recommend
→ Interested? Use /learn [role]
→ Want details? Use /explore-roles [role]
→ Check fit? Use /assess [role]
```
