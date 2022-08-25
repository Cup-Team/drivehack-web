import styles from "../../styles/Main.module.css";
import Link from "next/link";
import Image from "next/image";

const Button = ({ id }) => {
  return (
    <Link href={`startup/${id}/`}>
      <div className={styles.additional}>
        Подробнее <Image src="/arrow.svg" width={128} height={18} />
      </div>
    </Link>
  );
};

export default Button;
