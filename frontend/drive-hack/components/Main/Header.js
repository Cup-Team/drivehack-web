import styles from "../../styles/Main.module.css";

const Header = () => {
  return (
    <div className={styles.header}>
      <a
        href="http://localhost:8000/startups/file"
        download
        className={styles.download}
      >
        Скачать CSV
      </a>
    </div>
  );
};
export default Header();
