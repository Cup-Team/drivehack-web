import styles from "../../styles/Main.module.css";

const Header = () => {
  return (
    <div className={styles.header}>
      <a href="/export.csv" download className={styles.download}>
        Скачать CSV
      </a>
    </div>
  );
};
export default Header;
