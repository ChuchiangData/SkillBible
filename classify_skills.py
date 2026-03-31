import json
import os
import re

json_path = "/Users/bluegrass/Desktop/Code-Project/SkillBible/skills_index.json"
output_md_path = "/Users/bluegrass/Desktop/Code-Project/SkillBible/skills_index_readme.md"

if not os.path.exists(json_path):
    print(f"Error: {json_path} not found.")
    exit(1)

with open(json_path, 'r', encoding='utf-8') as f:
    skills = json.load(f)

# Define 15 key categories and comprehensive keywords for matching
categories = {
    "AI & Machine Learning": [r"\bai\b", "llm", "agent", "machine learning", "rag", "prompt", "langchain", "crewai", "hugging-face", r"\bml\b", "chatbot", "gpt", "model", "vector", r"\bmcp\b", "anthropic", "openai", "claude"],
    "Frontend Development": ["frontend", "react", "angular", "vue", "ui", "css", "html", "nextjs", "svelte", "component", "javascript", "typescript", "tailwind"],
    "Backend Development": ["backend", "api", "django", "rails", "fastapi", "nestjs", "node", "express", "spring", "flask", r"c#", "dotnet", "java", "ruby", "php", "elixir", "graphql", "rest"],
    "Security & Pentesting": ["security", "pentest", "vulnerability", "hack", "exploit", "audit", "xss", "sqli", "owasp", "auth", "malware", "cve", "burp", "red-team", "threat"],
    "DevOps & Cloud Infrastructure": ["devops", "aws", "azure", "kubernetes", "docker", "terraform", "ci/cd", "deployment", "cloud", "serverless", "infrastructure", "ansible"],
    "Database & Analytics": ["database", "sql", "postgres", "mongodb", "analytics", "data engineer", "data science", "dbt", "pandas", "redshift", "redis", "elastic"],
    "Mobile & Multi-platform": ["mobile", "ios", "android", "flutter", "react native", "react-native", "expo", "swift", "kotlin", "app store"],
    "Design & UX": ["design", "ui/ux", "ux", "figma", "brand", "canva", "art", "creative", "layout", "visual"],
    "Productivity & Office": ["office", "word", "excel", "pdf", "docx", "xlsx", "pptx", "libreoffice", "document", "presentation"],
    "Marketing & Growth": ["seo", "marketing", "apify", "scrape", "tiktok", "youtube", "twitter", "audience", "lead generation", "ads", "campaign"],
    "Game & 3D Development": ["game", "unity", "godot", "unreal", "3d", "2d", "gaming", "threejs"],
    "System, Go, & System OS": ["bash", "linux", "os", r"\bkernel\b", "powershell", "shell", "rust", "cpp", r"c\+\+", "operating system", r"\bc\b", r"\bgo\b", "golang"],
    "Workflow & Automation": ["zapier", "make", "n8n", "automation", "workflow", "automate", "bot", "discord", "slack-automation"],
    "Architecture & Documentation": ["architecture", "docs", "c4", "wiki", "readme", "decision", "pattern", "systematic"]
}

def guess_category(item):
    # Combine title, description and current category for robust searching
    text = (item.get('name', '') + ' ' + item.get('description', '')).lower()
    
    best_match = "Miscellaneous / Other"
    max_score = 0
    
    for cat, keywords in categories.items():
        score = 0
        for kw in keywords:
            if kw.startswith(r"\b"):
                score += len(re.findall(kw, text))
            else:
                escaped = re.escape(kw)
                # Count exact word boundaries generally for all other keywords to avoid partial matches
                # e.g. "ui" matching inside "build"
                score += len(re.findall(r'\b' + escaped + r'\b', text))
        
        if score > max_score:
            max_score = score
            best_match = cat
            
    # Some items are so ambiguous, fallback manually or keep current category if it was somewhat good,
    # but initially they are mostly "uncategorized".
    return best_match

for item in skills:
    cat = guess_category(item)
    # Re-assign
    item['category'] = cat

# Make sure all items have names and descriptions (handle edge cases)
for item in skills:
    if 'name' not in item:
        item['name'] = item.get('id', 'Unknown')
    if 'description' not in item:
        item['description'] = 'No description.'

# Save back to JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(skills, f, indent=2, ensure_ascii=False)

print(f"Updated {json_path} successfully!")

# Group for README
grouped_skills = {}
for item in skills:
    cat = item.get('category', 'Miscellaneous / Other')
    grouped_skills.setdefault(cat, []).append(item)

with open(output_md_path, 'w', encoding='utf-8') as f:
    f.write("# 📚 Skills Index\n\n")
    f.write("A comprehensive, auto-categorized index of all available skills in this repository. Use this to quickly find specialized agents and instruction sets for any task.\n\n")
    
    # TOC
    f.write("## 🗂 Categories\n\n")
    for cat in sorted(grouped_skills.keys()):
        anchor = cat.lower().replace(' & ', '').replace(' ', '-').replace(',', '').replace('/', '')
        f.write(f"- [{cat} ({len(grouped_skills[cat])})](#{anchor})\n")
    f.write("\n---\n\n")
    
    for cat in sorted(grouped_skills.keys()):
        f.write(f"## {cat}\n\n")
        f.write("<details>\n<summary>Click to expand {len(grouped_skills[cat])} skills</summary>\n\n")
        f.write("| Skill Name | Description |\n")
        f.write("|------------|-------------|\n")
        
        # Sort skills within category by name ALPHABETICALLY
        for item in sorted(grouped_skills[cat], key=lambda x: x['name']):
            name = item['name']
            path = item.get('path', f"skills/{name}")
            
            # Escape pipes to avoid breaking MD tables
            desc = item['description'].replace('\n', ' ').replace('|', '\\|')
            if len(desc) > 150:
                desc = desc[:147] + "..."
                
            f.write(f"| [`{name}`]({path}) | {desc} |\n")
        
        f.write("\n</details>\n\n")
    
print(f"Generated {output_md_path} successfully!")
