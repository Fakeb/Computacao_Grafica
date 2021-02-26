
import javax.swing.JOptionPane;

/**
 *
 * @author Rafael Cancian e Rafael Meneses
 */

public class MainFrame extends javax.swing.JFrame {

    int tipoTransformacao = -1;

    public MainFrame() {
        initComponents();
        setLocationRelativeTo(null);
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPane1 = new javax.swing.JScrollPane();
        jTableMatriz = new javax.swing.JTable();
        jTextValorX = new javax.swing.JTextField();
        jLabelResultado = new javax.swing.JLabel();
        jTextValorY = new javax.swing.JTextField();
        jComboOpcoes = new javax.swing.JComboBox<>();
        jButtonCalcular = new javax.swing.JButton();
        jTextStatusTransformacao = new javax.swing.JTextField();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Transformações Geométricas 2D");
        setPreferredSize(new java.awt.Dimension(395, 375));
        setResizable(false);

        jTableMatriz.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        jTableMatriz.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                { new Float(1.0),  new Float(0.0),  new Float(0.0)},
                { new Float(0.0),  new Float(1.0),  new Float(0.0)},
                { new Float(0.0),  new Float(0.0),  new Float(1.0)}
            },
            new String [] {
                "Coluna 1", "Coluna 2", "Coluna 3"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Float.class, java.lang.Float.class, java.lang.Float.class
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }
        });
        jTableMatriz.setRowHeight(30);
        jTableMatriz.setShowGrid(true);
        jTableMatriz.setTableHeader(null);
        jScrollPane1.setViewportView(jTableMatriz);

        jTextValorX.setBackground(new java.awt.Color(240, 240, 240));
        jTextValorX.setHorizontalAlignment(javax.swing.JTextField.CENTER);
        jTextValorX.setText("0");
        jTextValorX.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)), "Valor de X:"));
        jTextValorX.setEnabled(false);

        jLabelResultado.setText("Insira os valores de X e de Y para mostrar o resultado da transformação:");

        jTextValorY.setBackground(new java.awt.Color(240, 240, 240));
        jTextValorY.setHorizontalAlignment(javax.swing.JTextField.CENTER);
        jTextValorY.setText("0");
        jTextValorY.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)), "Valor de Y:"));
        jTextValorY.setEnabled(false);

        jComboOpcoes.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        jComboOpcoes.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Translação", "Rotação", "Escala", "Próxima etapa" }));
        jComboOpcoes.setSelectedIndex(-1);
        jComboOpcoes.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jComboOpcoesActionPerformed(evt);
            }
        });

        jButtonCalcular.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        jButtonCalcular.setText("CALCULAR");
        jButtonCalcular.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonCalcularActionPerformed(evt);
            }
        });

        jTextStatusTransformacao.setEditable(false);
        jTextStatusTransformacao.setBackground(new java.awt.Color(240, 240, 240));
        jTextStatusTransformacao.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        jTextStatusTransformacao.setHorizontalAlignment(javax.swing.JTextField.CENTER);
        jTextStatusTransformacao.setText("N/A");
        jTextStatusTransformacao.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)), "Última transformação realizada:"));

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                    .addComponent(jComboOpcoes, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jButtonCalcular, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jLabelResultado, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(jTextValorX, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jTextValorY, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(81, 81, 81)))
                        .addGap(0, 25, Short.MAX_VALUE))
                    .addComponent(jTextStatusTransformacao))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 92, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextStatusTransformacao, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabelResultado)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jTextValorX, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jTextValorY, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 28, Short.MAX_VALUE)
                .addComponent(jComboOpcoes, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jButtonCalcular)
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButtonCalcularActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonCalcularActionPerformed
        switch (jComboOpcoes.getSelectedIndex()) {
            case 0: {
                desabilitarFields();
                tipoTransformacao = calcularTranslacao();
                break;
            }
            case 1: {
                desabilitarFields();
                tipoTransformacao = calcularRotacao();
                break;
            }
            case 2: {
                desabilitarFields();
                tipoTransformacao = calcularEscala();
                break;
            }
            case 3: {
                habilitarFields();
                calcularProximaEtapa();
                break;
            }
        }
    }//GEN-LAST:event_jButtonCalcularActionPerformed

    private void jComboOpcoesActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jComboOpcoesActionPerformed
        switch (jComboOpcoes.getSelectedIndex()) {
            case 0: {
                desabilitarFields();
                break;
            }
            case 1: {
                desabilitarFields();
                break;
            }
            case 2: {
                desabilitarFields();
                break;
            }
            case 3: {
                habilitarFields();
                break;
            }
        }
    }//GEN-LAST:event_jComboOpcoesActionPerformed

    public int calcularTranslacao() {
        float Tx = Float.parseFloat(JOptionPane.showInputDialog(this, "Digite o valor de Tx:"));
        jTableMatriz.setValueAt(Tx, 0, 2);
        float Ty = Float.parseFloat(JOptionPane.showInputDialog(this, "Digite o valor de Ty:"));
        jTableMatriz.setValueAt(Ty, 1, 2);

        jTableMatriz.setValueAt(1, 0, 0);
        jTableMatriz.setValueAt(1, 1, 1);
        jTableMatriz.setValueAt(0, 0, 1);
        jTableMatriz.setValueAt(0, 1, 0);

        jTextStatusTransformacao.setText("Translação");

        return 0;
    }

    public int calcularRotacao() {
        float anguloTeta = Float.parseFloat(JOptionPane.showInputDialog(this, "Digite o ângulo teta:"));
        jTableMatriz.setValueAt((float) Math.cos(Math.toRadians(anguloTeta)), 0, 0);
        jTableMatriz.setValueAt((float) -Math.sin(Math.toRadians(anguloTeta)), 0, 1);
        jTableMatriz.setValueAt((float) Math.sin(Math.toRadians(anguloTeta)), 1, 0);
        jTableMatriz.setValueAt((float) Math.cos(Math.toRadians(anguloTeta)), 1, 1);

        jTableMatriz.setValueAt(0, 0, 2);
        jTableMatriz.setValueAt(0, 1, 2);

        jTextStatusTransformacao.setText("Rotação");

        return 1;
    }

    public int calcularEscala() {
        float Sx = Float.parseFloat(JOptionPane.showInputDialog(this, "Digite o valor de Sx:"));
        jTableMatriz.setValueAt(Sx, 0, 0);
        float Sy = Float.parseFloat(JOptionPane.showInputDialog(this, "Digite o valor de Sy:"));
        jTableMatriz.setValueAt(Sy, 1, 1);

        jTableMatriz.setValueAt(0, 0, 2);
        jTableMatriz.setValueAt(0, 1, 2);
        jTableMatriz.setValueAt(0, 0, 1);
        jTableMatriz.setValueAt(0, 1, 0);

        jTextStatusTransformacao.setText("Escala");

        return 2;
    }

    public void calcularProximaEtapa() {
        switch (tipoTransformacao) {
            case 0: {
                //Translação
                float Tx = (float) jTableMatriz.getValueAt(0, 2);
                float Ty = (float) jTableMatriz.getValueAt(1, 2);
                float x = Float.parseFloat(jTextValorX.getText());
                float y = Float.parseFloat(jTextValorY.getText());

                JOptionPane.showMessageDialog(this, "O resultado é: (" + (Tx + x) + ", " + (Ty + y) + ")");
                break;
            }
            case 1: {
                //Rotação
                float cosTeta = (float) jTableMatriz.getValueAt(0, 0);
                float senTeta = (float) jTableMatriz.getValueAt(1, 0);

                float x = Float.parseFloat(jTextValorX.getText());
                float y = Float.parseFloat(jTextValorY.getText());

                float Xu = x * cosTeta - y * senTeta;
                float Yu = y * cosTeta + x * senTeta;

                JOptionPane.showMessageDialog(this, "O resultado é: (" + Xu + ", " + Yu + ")");
                break;
            }
            case 2: {
                //Escala
                float Sx = (float) jTableMatriz.getValueAt(0, 0);
                float Sy = (float) jTableMatriz.getValueAt(1, 1);
                float x = Float.parseFloat(jTextValorX.getText());
                float y = Float.parseFloat(jTextValorY.getText());

                JOptionPane.showMessageDialog(this, "O resultado é: (" + (Sx * x) + ", " + (Sy * y) + ")");
                break;
            }
            default: {
                JOptionPane.showMessageDialog(this, "ERRO: Nenhuma transformação foi encontrada.", "Mensagem de erro", JOptionPane.ERROR_MESSAGE);
                break;
            }
        }
    }
    
    public void habilitarFields() {
        jTextValorX.setEnabled(true);
        jTextValorY.setEnabled(true);
    }
    
    public void desabilitarFields() {
        jTextValorX.setEnabled(false);
        jTextValorY.setEnabled(false);
    }

    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Windows".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new MainFrame().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButtonCalcular;
    private javax.swing.JComboBox<String> jComboOpcoes;
    private javax.swing.JLabel jLabelResultado;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable jTableMatriz;
    private javax.swing.JTextField jTextStatusTransformacao;
    private javax.swing.JTextField jTextValorX;
    private javax.swing.JTextField jTextValorY;
    // End of variables declaration//GEN-END:variables
}
