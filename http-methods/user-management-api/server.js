const express = require("express");
const app = express();
const cors = require("cors");
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON bodies
app.use(express.json());

// CORS middleware to allow all origins
app.use(cors());

// Data store (temporary in-memory store)
let users = [];

// Endpoint for creating a new user (POST /users)
app.post("/users", (req, res) => {
  const { name, email, password } = req.body;
  const newUser = { id: users.length + 1, name, email, password };
  users.push(newUser);
  res.status(201).json(newUser);
});

// Endpoint for updating an existing user (PUT /users/:id)
app.put("/users/:id", (req, res) => {
  const userId = parseInt(req.params.id);
  const { name, email, password } = req.body;
  const userIndex = users.findIndex((user) => user.id === userId);
  if (userIndex !== -1) {
    users[userIndex] = { id: userId, name, email, password };
    res.status(200).json(users[userIndex]);
  } else {
    res.status(404).json({ message: "User not found" });
  }
});

// Serve static files from the 'public' directory
app.use(express.static("public"));

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
