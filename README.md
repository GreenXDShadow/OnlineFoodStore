# OnlineFoodStore
CMPE-131 Group Project

## User Guide: Contributing to the OnlineFoodStore Repository

### Prerequisites:
1. Ensure you have `git` installed on your machine. If not, [download and install it](https://git-scm.com/downloads).

### 2. **Clone the Repository**:
Now, clone the repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/OnlineFoodStore.git
```
Replace `YOUR_USERNAME` with your GitHub username.

### 2. **Set the Upstream**:
Navigate to the cloned directory:

```bash
cd OnlineFoodStore
```

Then, set up the original repository as the `upstream`:

```bash
git remote add upstream https://github.com/GreenXDShadow/OnlineFoodStore.git
```

### 3. **Pull the Latest Changes**:
Before making any changes, ensure you have the latest version from the original repository:

```bash
git pull upstream staging
```

### 4. **Create a New Branch**:
Always create a new branch for your changes. This keeps the workflow clean:

```bash
git checkout -b feature/NAME_OF_YOUR_FEATURE
```
Replace `NAME_OF_YOUR_FEATURE` with a brief name that describes your changes.

### 5. **Make Your Changes**:
Modify, add, or delete files as necessary for your feature or fix.

### 6. **Commit Your Changes**:
Once you've made your changes, commit them:

```bash
git add .
git commit -m "Brief description of your changes"
```

### 7. **Push to Your Fork**:
Push your changes to your fork:

```bash
git push origin feature/NAME_OF_YOUR_FEATURE
```

### 8. **Create a Pull Request (PR)**:
Finally, create a pull request to the `staging` branch of the original `OnlineFoodStore` repository:

- Go to your forked repository on GitHub.
- Click on the **New pull request** button.
- Ensure the base repository is `GreenXDShadow/OnlineFoodStore` and the base branch is `staging`.
- For the head repository, choose your fork and the branch you just pushed.
- Click **Create pull request**.
- Fill in a title and description for your PR, then submit.

---

Once you've submitted your PR, your changes will be reviewed. If everything looks good, they will merge your changes into the `staging` branch. Nick will then take care of pushing the changes to the `main` branch.
