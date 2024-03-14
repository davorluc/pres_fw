# Motivation
The reason this repo exists is because me as a long-time student was tired of always using PowerPoint presentations. I wanted a quick way to create powerful and creative presentations with minimal effort. What better way is there other than writing markdown files?

I stumbled upon [reveal.js](https://github.com/hakimel/reveal.js) some time ago, but found the conventional way of using it rather exhausting. So I configured it to my own liking where it simplifies the use of markdown slides.

# Setup
**IMPORTANT**
I recommend you creating a new repo for your presentation and adding this very repo as a submodule to your repo. 
You can add it like this:
```
git submodule add https://github.com/davorluc/pres_fw.git
```

The cloning might take a while, since the reveal.js repo is pretty big. I have removed some example files to make it a little lighter and changed some things inside the index.html file to make it Markdown compatible from the start.

---

## How others can access your presentation

If you were to clone your colleagues repo normally, the `pres_fw` directory would be empty. That's because we have to tell git explicitly to also clone submodules from a repo. You can modify the clone command as follows:
```
git clone --recursive https://github.con/davorluc/pres_fw.git
```

Again, that'll take a while. Please sit back and relax. Now that everything is set up you can add your slides as a markdown file

---
# Getting Started
## Where to save slides


This tool is very specific on how it wants your slides to be saved. Please save your Markdown slides under `[your_repo]/slides.md`. Everything else will make this tool fail.

## Where to save images for slides
Images must be saved under the `[your_repo]/img/` directory. `prepFiles.py` will prep the slides and images accordingly, since reveal.js wouldn't be able to reach the necessary files otherwise.

*Side note: After every change made to the `slides.md` file and `/img` directory you will need to re-run the step below*

---

# Starting a presentation

Now that everything is set up and you have your Markdown slides ready, it's time to start the presentation. Inside your terminal navigate to the reveal.js-master directory with cd

```
cd pres_fw
cd reveal.js
```

Then install all dependencies

```
npm install
```

And the last step:

```
npm start
```

From there you will receive a `http://localhost:8000` link in your terminal. Click on it to open the slides.

---

## Slide separation

I have used the `---` separator to let reveal.js know I want to start a regular new slide and the`-v-` separator to let reveal.js know i want to start a new vertical slide. If you don't know what the difference is, I'd highly recommend you look it up in the [reveal.js documentation](https://revealjs.com/vertical-slides/)

---

## Plugins

reveal.js offers a variety of built-in plugins. I have enabled the following:
- RevealHighlight
- RevealMarkdown
- RevealNotes
- RevealMath
- RevealZoom

To find out more, visit the [reveal.js documentation](https://revealjs.com)

---

I hope that this `README` has been informative enough for you to start using it. If questions arise or you notice some bugs, don't hesitate to get in touch with me or open a new issue under the issues tab. See ya around!
