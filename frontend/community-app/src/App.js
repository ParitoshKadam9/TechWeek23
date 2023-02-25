import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import './App.css';
import Communities from "./pages/community/Communities";
import Home from './pages/home/Home';
import Login from './pages/login/Login';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Login />
  },
  {
    path: "/home",
    element: <Home />
  },
  {
    path: "/communities",
    element: <Communities />
  }
]);

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;