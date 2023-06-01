# davorluc's presentation framework (using reveal.js)
Hello there! I'm glad you have found this repo. The reason I created this repo is as a helper repo for my reveal.js presentations. I want to be able to share my presentations with my classmates and colleagues so they can work on them too. It has been tricky with using the [reveal.js](https://github.com/hakimel/reveal.js) repo as a submodule so far, since all the changes I do locally aren't transferred to my colleagues. I haven't figured out a way to fix this yet, so I am trying this approach

# Setup
The setup is very straight forward. First you create your own github repo (if you don't know how, I'm sure there is someone on YouTube that can explain it to you) or you clone the existing Github repo from your colleague using

```
git clone <github repo url here>
```

---

**If you are the creator of the above mentioned repo please read this part, the others may continue to the next**

Now that you have created your own Github repo and have successfully cloned it to your repo, time to add this very repo as a submodule to your repo.

```
git submodule add https://github.com/davorluc/pres_fw
```

The cloning might take a while, since the reveal.js repo is pretty big. I have removed some example files to make it a little lighter and changed some things inside the index.html file to make it Markdown compatible from the start.

---

**If you are the collaborator or aren't cloning the personal repo for the first time please read this part**

After cloning your colleagues repo, you'll see there is a *pres_fw* folder, but it is emtpy. That's because this repo is a submodule of your repo (if you haven't worked with submodules yet, you can imagine it like a link). We have to tell Git explicitly to also clone the content of my *pres_fw* repo into your repo. We can do this with:

```
git submodule update -i -r
```

Again, that'll take a while. Please sit back and relax.


