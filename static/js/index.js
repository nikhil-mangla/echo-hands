// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyDhnHxUWFJm2nYf2RLAn_84vTvjc0YH5N8",
  authDomain: "echo-hands-90b8d.firebaseapp.com",
  databaseURL: "https://echo-hands-90b8d-default-rtdb.firebaseio.com",
  projectId: "echo-hands-90b8d",
  storageBucket: "echo-hands-90b8d.appspot.com",
  messagingSenderId: "927820701687",
  appId: "1:927820701687:web:a9719cd9c823316a6f98f2",
  measurementId: "G-C8ZHEZB6WY"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Initialize variables
const auth = firebase.auth();
const database = firebase.database();

// Set up our register function
function register() {
  // Get input fields
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const full_name = document.getElementById('full_name').value;

  // Validate input fields
  if (!validate_email(email) || !validate_password(password)) {
    alert('Email or Password is Out of Line!');
    return; // Stop the function if validation fails
  }

  if (!validate_field(full_name)) {
    alert('Name field is Out of Line!');
    return; // Stop the function if validation fails
  }

  // Move on with Authentication
  auth.createUserWithEmailAndPassword(email, password)
    .then(function () {
      // Get the current user
      const user = auth.currentUser;

      // Reference to the Firebase Database
      const database_ref = database.ref();

      // Create User data
      const user_data = {
        email: email,
        full_name: full_name,
        last_login: Date.now()
      };

      // Push user data to Firebase Database
      database_ref.child('users/' + user.uid).set(user_data);

      // Show success alert
      alert('User Created!');
    })
    .catch(function (error) {
      // Handle Errors
      const error_code = error.code;
      const error_message = error.message;

      alert(error_message);
    });
}

// Set up our login function
function login() {
  // Get input fields
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  // Validate input fields
  if (!validate_email(email) || !validate_password(password)) {
    alert('Email or Password is Out of Line!');
    return; // Stop the function if validation fails
  }

  auth.signInWithEmailAndPassword(email, password)
    .then(function () {
      // Get the current user
      const user = auth.currentUser;

      // Reference to the Firebase Database
      const database_ref = database.ref();

      // Update user data with last login time
      const user_data = {
        last_login: Date.now()
      };

      // Push the updated data to Firebase Database
      database_ref.child('users/' + user.uid).update(user_data);

      // Show success alert
      alert('User Logged In!');

      // Redirect to the /predict route after successful login
      window.location.href = "/predict";  // Flask route for prediction
    })
    .catch(function (error) {
      // Handle Errors
      const error_code = error.code;
      const error_message = error.message;

      alert(error_message);
    });
}


// Validate Functions
function validate_email(email) {
  const expression = /^[^@]+@\w+(\.\w+)+\w$/;
  return expression.test(email);
}

function validate_password(password) {
  // Firebase only accepts passwords greater than 6 characters
  return password.length >= 6;
}

function validate_field(field) {
  return field != null && field.length > 0;
}