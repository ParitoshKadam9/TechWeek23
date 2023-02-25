import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import './App.css';
import Communities from "./pages/community/Communities";
import Community from "./pages/community/Community";
import Error from "./pages/Error";
import Home from './pages/home/Home';
import Login from './pages/login/Login';
import Profile from "./pages/profile/Profile";
import Signup from "./pages/signup/Signup";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Login />,
    errorElement: <Error />
  },
  {
    path: "/signup",
    element: <Signup />
  },
  {
    path: "/home",
    element: <Home />
  },
  {
    path: "/communities",
    element: <Communities />
  },
  {
    path: "/community/:communityID",
    element: <Community />
  },
  {
    path: "/profile/:userID",
    element: <Profile />
  }
]);

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;