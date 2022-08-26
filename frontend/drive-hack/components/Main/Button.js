import styles from "../../styles/Main.module.css";
import Link from "next/link";
import Image from "next/image";

const Button = ({ id }) => {
  return (
    <Link href={`startup/${id}/`}>
      <div className={styles.additional}>
        Подробнее{" "}
        <div className={styles.arrow}>
          <Image src="/arrow.svg" layout="fill" />
        </div>
      </div>
    </Link>
  );
};

export default Button;
