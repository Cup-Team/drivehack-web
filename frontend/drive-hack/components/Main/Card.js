import styles from "../../styles/Main.module.css";
import Button from "./Button.js";

const Card = ({ title, description, mentions, media }) => {
  return (
    <div className={styles.card}>
      <div>
        <h2 style={{ marginBottom: "1vw" }}>{title}</h2>{" "}
        <p className={styles.description}>{description}</p>
      </div>
      <div className={styles.statsWrapper}>
        <div className={styles.stats}>
          <p style={{ marginRight: "2vw" }}>
            <mark>{mentions}</mark> упомининий
          </p>
          <p>
            <mark>{media}</mark> сми
          </p>
        </div>
        <Button id={1} />
      </div>
    </div>
  );
};

export default Card;
