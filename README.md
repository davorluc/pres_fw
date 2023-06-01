# davorluc's presentation framework (using reveal.js)
Hello there! I'm glad you have found this repo. The reason I created this repo is as a helper repo for my reveal.js presentations. I want to be able to share my presentations with my classmates and colleagues so they can work on them too. It has been tricky with using the [reveal.js](https://github.com/hakimel/reveal.js) repo as a submodule so far, since all the changes I do locally aren't transferred to my colleagues. I haven't figured out a way to fix this yet, so I am trying this approach

# Setup
The setup is very straight forward. First you create your own github repo (if you don't know how, I'm sure there is someone on YouTube that can explain it to you) or you clone the existing Github repo from your colleague using

```
git clone <github repo url here>
```

---

## **If you are the creator of the above mentioned repo please read this part, the others may continue to the next**

Now that you have created your own Github repo and have successfully cloned it to your repo, time to add this very repo as a submodule to your repo.

```
git submodule add https://github.com/davorluc/pres_fw.git
```

The cloning might take a while, since the reveal.js repo is pretty big. I have removed some example files to make it a little lighter and changed some things inside the index.html file to make it Markdown compatible from the start.

---

**## If you are the collaborator or aren't cloning the personal repo for the first time please read this part**

If you were to clone your colleagues repo normally, the `pres_fw` directory would be empty. That's because we have to tell git explicitly to also clone submodules from a repo. You can modify the clone command as follows:
```
git clone --recursive https://github.con/davorluc/pres_fw.git
```

Again, that'll take a while. Please sit back and relax. Now that everything is set up you can add your slides as a markdown file

---

## Where to store your slides

Inside the index.html, the location of the `slides.md` file is `../../slides.md`. It'll spit out an error if we just leave if like that. That's why I wrote a short python script `copyMarkdown.py` that copies the markdown file from `../..slides.md` to the current directory.

For that, make sure you're in the `reveal.js` directory, then execute:

```
python3 copyMarkdown.py
```

After that everything should work as normal. Don't forget after you adjusted your slides.md file to always run the `copyMarkdown.py` script again to make sure reveal.js always reads the newest version of your slides.

---

## Starting a presentation

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
