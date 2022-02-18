
SELECT SUM(credito_solicitado) as soma_credito, day FROM ( /* Agrupa as solicitações por dia somando os créditos */
SELECT id, name, idade, credito_solicitado, CAST(data_solicitacao as DATE) as day FROM ( 
  SELECT *, /* Filtra solicitações duplicadas por nome (cliente) mantendo a última data */
    RANK() OVER (PARTITION BY name ORDER BY data_solicitacao DESC) dest_rank
    FROM `keycashtest.keycash_dataset.LANDING_TABLE`
  ) WHERE dest_rank = 1 )
  GROUP BY day

  
