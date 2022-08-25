import "../styles/globals.css";
import Sidebar from "../components/Sidebar.js";

function MyApp({ Component, pageProps }) {
  return (
    <Sidebar>
      <Component {...pageProps} />
    </Sidebar>
  );
}

export default MyApp;
