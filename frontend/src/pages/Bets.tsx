
import { useCallback, useEffect, useState } from "react";
import { fetchBets, fetchBetAudit } from "../api/client";
import { AuditPanel } from "../components/AuditPanel";

interface Bet {
  id: string;
  stake: number;
  odds: number;
}

interface BetAudit {
  id: string;
  [key: string]: unknown;
}

export function Bets() {
  const [bets, setBets] = useState<Bet[]>([]);
  const [audit, setAudit] = useState<BetAudit[]>([]);
  const [selectedBetId, setSelectedBetId] = useState<string | null>(null);

  const [isLoading, setIsLoading] = useState(true);
  const [isAuditLoading, setIsAuditLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [auditError, setAuditError] = useState<string | null>(null);

  const loadBets = useCallback(async () => {
    try {
      setIsLoading(true);
      setError(null);

      const data: Bet[] = await fetchBets();
      setBets(data);
    } catch (err) {
      console.error("Failed to fetch bets:", err);
      setError("Unable to load bets. Please try again.");
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    void loadBets();
  }, [loadBets]);

  const handleViewAudit = async (betId: string) => {
    setSelectedBetId(betId);
    setAudit([]);
    setAuditError(null);
    setIsAuditLoading(true);

    try {
      const data: BetAudit[] = await fetchBetAudit(betId);

      setAudit(data);
    } catch (err) {
      console.error(`Failed to fetch audit for bet ${betId}:`, err);
      setAuditError("Unable to load audit history.");
    } finally {
      setIsAuditLoading(false);
    }
  };

  if (isLoading) {
    return <p role="status">Loading bets...</p>;
  }

  if (error) {
    return (
      <div role="alert">
        <p>{error}</p>
        <button type="button" onClick={() => void loadBets()}>
          Retry
        </button>
      </div>
    );
  }

  return (
    <section aria-labelledby="bets-heading">
      <header>
        <h2 id="bets-heading">Bets</h2>
        <p>View and manage bet records and audit history.</p>
      </header>

      {bets.length === 0 ? (
        <p>No bets found.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Stake</th>
              <th scope="col">Odds</th>
              <th scope="col">Audit</th>
            </tr>
          </thead>

          <tbody>
            {bets.map((bet) => (
              <tr key={bet.id}>
                <td>{bet.id}</td>
                <td>{bet.stake.toLocaleString()}</td>
                <td>{bet.odds.toFixed(2)}</td>
                <td>
                  <button
                    type="button"
                    onClick={() => void handleViewAudit(bet.id)}
                    disabled={isAuditLoading}
                    aria-label={`View audit history for bet ${bet.id}`}
                  >
                    View Audit
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {selectedBetId !== null && (
        <section aria-label={`Audit history for bet ${selectedBetId}`}>
          <h3>Audit History</h3>
      )}
    </section>
  );
}
