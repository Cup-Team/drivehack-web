import Link from "next/link";

const Sidebar = ({ children }) => {
  return (
    <>
      <main>
        <aside>
          <nav></nav>
        </aside>
        {children}
      </main>
    </>
  );
};

export default Sidebar;
