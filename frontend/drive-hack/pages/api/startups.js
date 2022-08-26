import { startups } from "./data/startups";

export default function handler(req, res) {
  res.status(200).json(startups);
}
