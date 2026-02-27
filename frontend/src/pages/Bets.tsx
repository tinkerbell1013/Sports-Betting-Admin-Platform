import { useEffect, useState } from "react";
import { fetchBets, fetchBetAudit } from "../api/client";
import { AuditPanel } from "../components/AuditPanel";

export function Bets() {
  const [bets, setBets] = useState<any[]>([]);
  const [audit, setAudit] = useState<any[]>([]);

  useEffect(() => {
    fetchBets().then(setBets);
  }, []);

  return (
    <div>
      <h2>Bets</h2>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Stake</th>
            <th>Odds</th>
            <th>Audit</th>
          </tr>
        </thead>
        <tbody>
          {bets.map(b => (
            <tr key={b.id}>
              <td>{b.id}</td>
              <td>{b.stake}</td>
              <td>{b.odds}</td>
              <td>
                <button onClick={() => fetchBetAudit(b.id).then(setAudit)}>
                  View Audit
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {audit.length > 0 && <AuditPanel audits={audit} />}
    </div>
  );
}
