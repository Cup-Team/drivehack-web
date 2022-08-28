import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);
const labels = ["Arrival", "Edge Vision", "Wanderu", "WalletKit", "WHILL"];
const data = {
  labels: labels,
  datasets: [
    {
      label: "Transport startups",
      data: [105, 37, 22, 62, 24],
      backgroundColor: "#652FFF",
    },
  ],
};

const Stats = () => {
  return (
    <div style={{ width: "50vw" }}>
      <Bar data={data} />
    </div>
  );
};

export default Stats;
