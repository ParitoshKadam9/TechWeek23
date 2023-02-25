import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Navbar from "../../components/navbar/Navbar";

const styles = {
  root: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
    backgroundColor: "#000000"
  },
  paper: {
    padding: "5%",
    textAlign: "center",
    color: "#333",
    width: "100vw",
    height: "80vh",
    backgroundColor: "#ffffff"
    //maxWidth: "800px",
  },
  avatar: {
    width: "10vw",
    height: "10vw",
    margin: "0 auto",
  },
  button: {
    margin: "12px",
  },
};

const ProfilePage = () => {
  return (
    <body>
    <Navbar/>
    <div style={styles.root}>
      <Paper elevation={3} style={styles.paper}>
        <Avatar
          alt="User Avatar"
          src="https://picsum.photos/200"
          style={styles.avatar}
        />
        <h1>User Name</h1>
        <p>User Bio</p>
        <Button variant="contained" color="primary" style={styles.button}>
          Edit Profile
        </Button>
      </Paper>
    </div>
    </body>
  );
};

export default ProfilePage;