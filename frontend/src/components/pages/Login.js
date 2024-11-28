import React, { useState } from "react";
import {
  Box,
  Container,
  Typography,
  TextField,
  Button,
  Grid,
  Link,
} from "@mui/material";
import AxiosInstance from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN,REFRESH_TOKEN } from "../../constants";

const Login = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const [errors, setErrors] = useState({});

  const handleChange = (evt) => {
    const { name, value } = evt.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const submission = (e) => {
    e.preventDefault();

    console.log("username -------->", formData.username)
    console.log("password -------->", formData.password)

    AxiosInstance.post(`auth/jwt/create/`, {
      username: formData.username,
      password: formData.password,
    })
      .then((res) => {
        console.log("response is ---------->", res);
        console.log("response is data access---------->", res.data.access);
        console.log("response is data refresh---------->", res.data.refresh);
        localStorage.setItem(ACCESS_TOKEN, res.data.access)
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh)
        navigate(`/`);
      })
      .catch((error) => {
        console.log("errors are ------>", error)
        if (error.response && error.response.data) {
          // Check if the error is a form validation error from the backend
          if (error.response.data.error) {
            setErrors({ general: error.response.data.error });
          } else {
            setErrors(error.response.data);
          }
        } else {
          setErrors({
            general: "An unexpected error occurred. Please try again.",
          });
        }
      });
  };

  return (
    <Container maxWidth="xs">
      <Box sx={{ mt: 4, mb: 2, textAlign: "center" }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Sign In
        </Typography>
        <Typography variant="body2" color="textSecondary">
          Log in into your account
        </Typography>
      </Box>

      <Box component="form" onSubmit={submission} noValidate sx={{ mt: 2 }}>
        {errors.general && (
          <Typography color="error" sx={{ mb: 2 }}>
            {errors.general}
          </Typography>
        )}

        <TextField
          label="User Name"
          name="username"
          margin="normal"
          fullWidth
          value={formData.username}
          onChange={handleChange}
          error={!!errors.username}
          helperText={errors.username}
          type="text"
          required
        />

        <TextField
          label="Password"
          name="password"
          margin="normal"
          fullWidth
          value={formData.password}
          onChange={handleChange}
          error={!!errors.password}
          helperText={errors.password}
          type="password"
          required
        />

        <Button
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          sx={{ mt: 2, mb: 2 }}
        >
          Login
        </Button>

        <Grid container justifyContent="flex-end">
          <Grid item>
            <Link href="/signup" variant="body2">
              Not have an account? Sign up
            </Link>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default Login;
