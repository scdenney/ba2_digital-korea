---
layout: default
title: Getting Started
---

<div class="page-layout">
  <aside class="page-sidebar">
    <div class="page-sidebar-inner">
      <h2 class="page-sidebar-title">On this page</h2>
      <nav class="page-toc">
        <ul>
          <li><a href="#before-the-first-class">Before the First Class</a></li>
          <li>
            <a href="#software-installation">Software Installation</a>
            <ul>
              <li><a href="#r-and-rstudio">R and RStudio</a></li>
              <li><a href="#swirl">Swirl</a></li>
              <li><a href="#orange-data-mining">Orange Data Mining</a></li>
            </ul>
          </li>
          <li>
            <a href="#github-setup">GitHub Setup</a>
            <ul>
              <li><a href="#creating-your-repository">Creating Your Repository</a></li>
              <li><a href="#repository-structure">Repository Structure</a></li>
              <li><a href="#submitting-your-repo-link">Submitting Your Repo Link</a></li>
            </ul>
          </li>
          <li>
            <a href="#working-with-markdown">Working with Markdown</a>
            <ul>
              <li><a href="#creating-markdown-files">Creating Markdown Files</a></li>
              <li><a href="#markdown-syntax">Markdown Syntax</a></li>
              <li><a href="#previewing-markdown">Previewing Markdown</a></li>
            </ul>
          </li>
        </ul>
      </nav>
    </div>
  </aside>

  <div class="page-content" markdown="1">

# Getting Started

This guide walks you through the software installation, GitHub setup, and basic skills you need for this course. Complete these steps before the first class.

---

## Before the First Class {#before-the-first-class}

Please complete the following installations before our first session so you are prepared for hands-on work:

1. **Install R and RStudio** - The programming environment for R tutorials
2. **Install Swirl** - Interactive R tutorials that run inside RStudio
3. **Install Orange Data Mining** - Our primary analysis tool for text-as-data work

Detailed instructions for each are below.

---

## Software Installation {#software-installation}

### R and RStudio {#r-and-rstudio}

R is a programming language for statistical computing. RStudio is the application you will use to work with R. You will not do anything sophisticated with R in this course, but you will be introduced to it through guided tutorials.

**Installation steps:**

1. Go to [posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/)
2. Download and install R for your operating system (follow Step 1 on the page)
3. Download and install RStudio Desktop (follow Step 2 on the page)
4. Open RStudio to verify the installation works

### Swirl {#swirl}

Swirl is an interactive tutorial system that runs inside RStudio. It provides hands-on R lessons directly in the console.

**Installation steps:**

1. Open RStudio
2. In the console (bottom-left panel), type the following and press Enter:
   ```r
   install.packages("swirl")
   ```
3. Load swirl by typing:
   ```r
   library(swirl)
   ```
4. Install the required courses by typing:
   ```r
   install_course("R Programming")
   install_course("Exploratory Data Analysis")
   ```
5. To start a lesson, type `swirl()` and follow the prompts

For more information, see [swirlstats.com/students.html](https://swirlstats.com/students.html)

### Orange Data Mining {#orange-data-mining}

Orange is our primary analysis tool. It is a visual, drag-and-drop platform for data analysis that makes computational methods accessible without programming.

**Installation steps:**

1. Go to [orangedatamining.com/download](https://orangedatamining.com/download/)
2. Download the installer for your operating system (Windows or macOS)
3. Run the installer and follow the prompts
4. Open Orange Data Mining
5. Install the Text add-on:
   - Go to **Options** in the menu bar
   - Select **Add-ons**
   - Find **Text** in the list and check the box
   - Click **OK** and restart Orange when prompted

The Text add-on provides the widgets we will use for text analysis throughout the course.

**Learning Orange:**

Throughout the course, you will work through Orange's official video tutorials. Bookmark these resources:

- **Getting Started Tutorials** (YouTube playlist): [Orange Getting Started](https://www.youtube.com/playlist?list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)
- **Widget Catalog**: [orangedatamining.com/widget-catalog](https://orangedatamining.com/widget-catalog/) — Your go-to reference when learning new widgets or troubleshooting

---

## GitHub Setup {#github-setup}

You will use GitHub to manage and submit your coursework. GitHub is a platform for version control and collaboration that is widely used in research and industry.

### Creating Your Repository {#creating-your-repository}

1. Create a GitHub account at [github.com](https://github.com) if you do not have one
2. Create a new **private** repository named: `BA2-DigitalKorea-<Surname>`
   - Replace `<Surname>` with your last name (e.g., `BA2-DigitalKorea-Kim`)
3. Add the instructor as a collaborator:
   - Go to your repository's **Settings**
   - Select **Collaborators** from the left menu
   - Click **Add people**
   - Enter the instructor's username: **scdenney**
   - Send the invitation

### Repository Structure {#repository-structure}

Organize your repository with the following folder structure:

```
DH-DigitalKorea-<Surname>/
├── assignments/
│   ├── week01/
│   │   ├── week01-deliverable.md
│   │   └── screenshots/
│   ├── week02/
│   │   └── ...
│   ├── week03/
│   │   └── ...
│   └── final-project/
└── README.md
```

**Guidelines:**

- Create a folder for each week's assignment (e.g., `week01/`, `week02/`)
- Place your deliverable markdown file and any screenshots in the appropriate folder
- Use the `README.md` file to introduce yourself and describe what your repository contains
- Keep the repository private unless you explicitly choose to share it

### Submitting Your Repo Link {#submitting-your-repo-link}

At the start of the course, submit the URL of your repository to the instructor. This allows the instructor to access your work for grading.

---

## Working with Markdown {#working-with-markdown}

Markdown is a lightweight markup language for formatting plain text. It allows you to create structured documents with headings, lists, links, and tables using simple syntax. Markdown files use the `.md` extension.

Markdown is widely used for documentation, GitHub repositories, and research workflows. Learning it is a transferable skill.

### Creating Markdown Files {#creating-markdown-files}

You can create Markdown files in any plain text editor. Here are instructions for the default editors on each platform:

**On macOS (TextEdit):**

1. Open TextEdit (press `Cmd + Space`, type "TextEdit", press Enter)
2. Switch to plain text mode: **Format** then **Make Plain Text** (or `Shift + Cmd + T`)
3. Write your content using Markdown syntax
4. Save with a `.md` extension: **File** then **Save**, enter a filename like `deliverable.md`

**On Windows (Notepad):**

1. Open Notepad (press `Windows + R`, type "notepad", press Enter)
2. Write your content using Markdown syntax
3. Save with a `.md` extension: **File** then **Save As**, enter the filename in quotes like `"deliverable.md"`, set **Save as type** to **All Files**, set **Encoding** to **UTF-8**

### Markdown Syntax {#markdown-syntax}

Here are the most common Markdown elements you will use:

**Headings:**
```markdown
# Heading 1
## Heading 2
### Heading 3
```

**Text formatting:**
```markdown
**bold text**
*italic text*
```

**Lists:**
```markdown
- Item one
- Item two
- Item three

1. First item
2. Second item
3. Third item
```

**Links:**
```markdown
[Link text](https://example.com)
```

**Images:**
```markdown
![Alt text](path/to/image.png)
```

**Code:**
```markdown
Inline `code` looks like this.
```

For a complete reference, see [markdownguide.org/basic-syntax](https://www.markdownguide.org/basic-syntax/)

### Previewing Markdown {#previewing-markdown}

Plain text editors show only the raw Markdown. To see the formatted output:

**Visual Studio Code (Recommended):**
- Open the `.md` file
- Press `Cmd + Shift + V` (macOS) or `Ctrl + Shift + V` (Windows) to preview
- Press `Cmd + K, V` (macOS) or `Ctrl + K, V` (Windows) for side-by-side view

**Other options:**
- **macOS:** MacDown, Marked 2
- **Cross-platform:** Obsidian, Typora
- **Browser-based:** [markdownlivepreview.com](https://markdownlivepreview.com)

**On GitHub:**
- GitHub automatically renders Markdown files when you view them in the browser
- This is the easiest way to check how your deliverables will look

  </div>
</div>
