import ExpImage from "next/future/image";
import Link from "next/link";
import styles from "../styles/Sidebar.module.css";
import { useRouter } from "next/router";

const navigation = [
  { id: 1, title: "Главная", path: "/" },
  { id: 2, title: "Статистика", path: "/stats" },
];

const Sidebar = ({ children }) => {
  const { pathname } = useRouter();
  return (
    <>
      <main>
        <aside>
          <ExpImage
            className={styles.logo}
            src="/logo.svg"
            width={67}
            height={61}
            layout="raw"
          />
          <nav>
            {navigation.map(({ title, path }, index) => (
              <Link href={path} key={index}>
                <a className={pathname === path ? styles.activeLink : null}>
                  {title}
                </a>
              </Link>
            ))}
          </nav>
        </aside>
        <div className={styles.mainWrapper}>{children}</div>
      </main>
    </>
  );
};

export default Sidebar;
