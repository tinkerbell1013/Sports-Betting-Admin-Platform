export async function fetchBets() {
  const res = await fetch("http://localhost:8000/bets");
  if (!res.ok) throw new Error("Failed to fetch bets");
  return res.json();
}

export async function fetchBetAudit(betId: number) {
  const res = await fetch(`http://localhost:8000/bets/${betId}/audit`);
  if (!res.ok) throw new Error("Failed to fetch audit");
  return res.json();
}
