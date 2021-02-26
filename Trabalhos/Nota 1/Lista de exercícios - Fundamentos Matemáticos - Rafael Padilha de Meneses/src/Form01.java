import javax.swing.ButtonModel;
import javax.swing.JOptionPane;
import java.lang.Math; 
import java.text.DecimalFormat;
import javax.swing.JFrame;
/*
    Programa 01 - Desenvolva um programa que leia pelo teclado os valores x, y e z de um vetor de 3 dimensões. Em seguida, apresente ao usuário um menu com as seguintes opções:
    1 -> Calcular o tamanho do vetor;
    2 -> Normalizar o vetor, apresentando o vetor resultante da normalização;
    3 -> Adicionar outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
    4 -> Subtrair outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
    5 -> Ler o valor de um escalar e realizar a multiplicação do mesmo pelo vetor, mostrando o vetor resultante;
    6 -> Ler o valor de um escalar e realizar a divisão do mesmo pelo vetor, mostrando o vetor resultante;
    7 -> Calcular o produto escalar do vetor lido anteriormente por outro vetor, lendo os valores x, y e z deste novo vetor e mostrando o resultado na tela.
 */

public class Form01 extends javax.swing.JFrame {
    
    DecimalFormat formatar = new DecimalFormat("0.00"); //metodo para formatar valor decimal com 2 casas depois da vírgula
    
    public Form01() {
        initComponents();
        jRadioButton_q01.setSelected(true);      
        setLocationRelativeTo(null);
    }
    
    public void questao01(){       
        double x = Math.pow(Double.parseDouble(jTextField_principalX.getText()),2); //valor de x ao quadrado
        double y = Math.pow(Double.parseDouble(jTextField_principalY.getText()),2); //valor de y ao quadrado
        double z = Math.pow(Double.parseDouble(jTextField_principalZ.getText()),2); //valor de z ao quadrado
        
        double resposta = Math.sqrt(x+y+z); // raiz quadrado da soma de x,y,z
        
        jTextArea_resultado.setText("O tamanho do Vetor é: " + formatar.format(resposta));            
    }
    
    public void questao02(){       
       
        double x = Math.pow(Double.parseDouble(jTextField_principalX.getText()),2); //valor de x ao quadrado
        double y = Math.pow(Double.parseDouble(jTextField_principalY.getText()),2); //valor de y ao quadrado
        double z = Math.pow(Double.parseDouble(jTextField_principalZ.getText()),2); //valor de z ao quadrado
        
        double resposta = Math.sqrt(x+y+z); // raiz quadrado da soma de x,y,z
        
        double v01 = Double.parseDouble(jTextField_principalX.getText())/resposta; // x dividido pelo tamanho do vetor
        double v02 = Double.parseDouble(jTextField_principalY.getText())/resposta; // y dividido pelo tamanho do vetor
        double v03 = Double.parseDouble(jTextField_principalZ.getText())/resposta; // z dividido pelo tamanho do vetor
        
        jTextArea_resultado.setText("Normalizando o Vetor < " + formatar.format(v01) + " , " + formatar.format(v02) + " , " + formatar.format(v03)+ " >");            
    }
    
    public void questao03(){                       
        double x = ( ( Double.parseDouble(jTextField_principalX.getText()) ) + ( Double.parseDouble(jTextField_secundarioX.getText()) ) );
        double y = ( ( Double.parseDouble(jTextField_principalY.getText()) ) + ( Double.parseDouble(jTextField_secundarioY.getText()) ) );
        double z = ( ( Double.parseDouble(jTextField_principalZ.getText()) ) + ( Double.parseDouble(jTextField_secundarioZ.getText()) ) );

        jTextArea_resultado.setText("O novo Vetor é: " + formatar.format(x) + " , " + formatar.format(y) + " , " + formatar.format(z));            
    }
    
    public void questao04(){                       
        double x = ( ( Double.parseDouble(jTextField_principalX.getText()) ) - ( Double.parseDouble(jTextField_secundarioX.getText()) ) );
        double y = ( ( Double.parseDouble(jTextField_principalY.getText()) ) - ( Double.parseDouble(jTextField_secundarioY.getText()) ) );
        double z = ( ( Double.parseDouble(jTextField_principalZ.getText()) ) - ( Double.parseDouble(jTextField_secundarioZ.getText()) ) );

        jTextArea_resultado.setText("O novo Vetor é: " + formatar.format(x) + " , " + formatar.format(y) + " , " + formatar.format(z));            
    }
    
    public void questao05(){                       
        double x = ( ( Double.parseDouble(jTextField_principalX.getText()) ) * ( Double.parseDouble(jTextField_escalar.getText()) ) );
        double y = ( ( Double.parseDouble(jTextField_principalY.getText()) ) * ( Double.parseDouble(jTextField_escalar.getText()) ) );
        double z = ( ( Double.parseDouble(jTextField_principalZ.getText()) ) * ( Double.parseDouble(jTextField_escalar.getText()) ) );

        jTextArea_resultado.setText("O novo Vetor é: " + formatar.format(x) + " , " + formatar.format(y) + " , " + formatar.format(z));            
    }
    
    public void questao06(){                       
        double x = ( ( Double.parseDouble(jTextField_principalX.getText()) ) / ( Double.parseDouble(jTextField_escalar.getText()) ) );
        double y = ( ( Double.parseDouble(jTextField_principalY.getText()) ) / ( Double.parseDouble(jTextField_escalar.getText()) ) );
        double z = ( ( Double.parseDouble(jTextField_principalZ.getText()) ) / ( Double.parseDouble(jTextField_escalar.getText()) ) );

        jTextArea_resultado.setText("O novo Vetor é: " + formatar.format(x) + " , " + formatar.format(y) + " , " + formatar.format(z));            
    }
    
    public void questao07(){                       
        double x = ( ( Double.parseDouble(jTextField_principalX.getText()) ) * ( Double.parseDouble(jTextField_secundarioX.getText()) ) );
        double y = ( ( Double.parseDouble(jTextField_principalY.getText()) ) * ( Double.parseDouble(jTextField_secundarioY.getText()) ) );
        double z = ( ( Double.parseDouble(jTextField_principalZ.getText()) ) * ( Double.parseDouble(jTextField_secundarioZ.getText()) ) );
        
        double resposta = (x+y+z);

        jTextArea_resultado.setText("O resultado do produto dos Vetores: " + formatar.format(resposta));            
    }
    
      
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup_programa01 = new javax.swing.ButtonGroup();
        jRadioButton_q01 = new javax.swing.JRadioButton();
        jRadioButton_q02 = new javax.swing.JRadioButton();
        jRadioButton_q03 = new javax.swing.JRadioButton();
        jRadioButton_q04 = new javax.swing.JRadioButton();
        jRadioButton_q05 = new javax.swing.JRadioButton();
        jRadioButton_q06 = new javax.swing.JRadioButton();
        jRadioButton_q07 = new javax.swing.JRadioButton();
        jPanel1 = new javax.swing.JPanel();
        jTextField_principalZ = new javax.swing.JTextField();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jTextField_principalX = new javax.swing.JTextField();
        jTextField_principalY = new javax.swing.JTextField();
        jPanel2 = new javax.swing.JPanel();
        jTextField_secundarioZ = new javax.swing.JTextField();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        jTextField_secundarioX = new javax.swing.JTextField();
        jTextField_secundarioY = new javax.swing.JTextField();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextArea_resultado = new javax.swing.JTextArea();
        jButton1 = new javax.swing.JButton();
        jTextField_escalar = new javax.swing.JTextField();
        jLabel1 = new javax.swing.JLabel();
        jButton2 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Programa 01");

        buttonGroup_programa01.add(jRadioButton_q01);
        jRadioButton_q01.setText("1 -> Calcular o tamanho do vetor;");

        buttonGroup_programa01.add(jRadioButton_q02);
        jRadioButton_q02.setText("2 -> Normalizar o vetor;");

        buttonGroup_programa01.add(jRadioButton_q03);
        jRadioButton_q03.setText("3 -> Adicionar outro vetor ao vetor Principal;");

        buttonGroup_programa01.add(jRadioButton_q04);
        jRadioButton_q04.setText("4 -> Subtrair outro vetor ao vetor Principal;");

        buttonGroup_programa01.add(jRadioButton_q05);
        jRadioButton_q05.setText("5 -> Ler o valor de um escalar e realizar a multiplicação pelo vetor Principal;");

        buttonGroup_programa01.add(jRadioButton_q06);
        jRadioButton_q06.setText("6 -> Ler o valor de um escalar e realizar a divisão pelo vetor Principal;");

        buttonGroup_programa01.add(jRadioButton_q07);
        jRadioButton_q07.setText("7 -> Calcular o produto escalar do vetor Principal com o Secundário.");

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createMatteBorder(3, 3, 3, 3, new java.awt.Color(153, 0, 153)), "Vetor Principal"));

        jLabel4.setText("Variavel X");

        jLabel5.setText("Variavel Y");

        jLabel6.setText("Variavel Z");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel4)
                    .addComponent(jTextField_principalX, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel5)
                    .addComponent(jTextField_principalY, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel6)
                    .addComponent(jTextField_principalZ, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(26, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addComponent(jLabel4)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextField_principalX, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel5)
                .addGap(5, 5, 5)
                .addComponent(jTextField_principalY, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel6)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextField_principalZ, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(12, Short.MAX_VALUE))
        );

        jPanel2.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createMatteBorder(3, 3, 3, 3, new java.awt.Color(153, 51, 0)), "Vetor Secundário"));

        jLabel7.setText("Variavel X");

        jLabel8.setText("Variavel Y");

        jLabel9.setText("Variavel Z");

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel7)
                    .addComponent(jTextField_secundarioX, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel8)
                    .addComponent(jTextField_secundarioY, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel9)
                    .addComponent(jTextField_secundarioZ, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(26, Short.MAX_VALUE))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addComponent(jLabel7)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextField_secundarioX, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(5, 5, 5)
                .addComponent(jLabel8)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextField_secundarioY, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel9)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextField_secundarioZ, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(12, Short.MAX_VALUE))
        );

        jTextArea_resultado.setColumns(20);
        jTextArea_resultado.setFont(new java.awt.Font("Times New Roman", 0, 18)); // NOI18N
        jTextArea_resultado.setRows(5);
        jScrollPane1.setViewportView(jTextArea_resultado);

        jButton1.setText("Calcular");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jLabel1.setText("Escalar");

        jButton2.setText("Programa 02");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(10, 10, 10)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jPanel2, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel1)
                                    .addComponent(jTextField_escalar, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jButton1))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jScrollPane1))
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jRadioButton_q06)
                                    .addComponent(jRadioButton_q07, javax.swing.GroupLayout.PREFERRED_SIZE, 395, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jRadioButton_q05)
                                    .addComponent(jRadioButton_q04)
                                    .addComponent(jRadioButton_q03)
                                    .addComponent(jRadioButton_q02)
                                    .addComponent(jRadioButton_q01))
                                .addGap(0, 0, Short.MAX_VALUE)))
                        .addGap(10, 10, 10))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jButton2)
                        .addGap(31, 31, 31))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(9, 9, 9)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jRadioButton_q01)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q02)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q03)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q04)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q05)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q06)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q07)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(17, 17, 17)
                                .addComponent(jLabel1)
                                .addGap(6, 6, 6)
                                .addComponent(jTextField_escalar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(10, 10, 10)
                                .addComponent(jButton1))
                            .addGroup(layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jButton2))
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(0, 8, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        
        
        if( !jTextField_principalX.getText().isEmpty() && !jTextField_principalY.getText().isEmpty() && !jTextField_principalZ.getText().isEmpty() ){
                      
            if(jRadioButton_q01.isSelected()){
                questao01();
            }
            else if(jRadioButton_q02.isSelected()){
                questao02();
            }
            else if(jRadioButton_q03.isSelected() && 
                    !jTextField_secundarioX.getText().isEmpty() && !jTextField_secundarioY.getText().isEmpty() && !jTextField_secundarioZ.getText().isEmpty() ){
                questao03();
            }
            else if(jRadioButton_q04.isSelected() && 
                    !jTextField_secundarioX.getText().isEmpty() && !jTextField_secundarioY.getText().isEmpty() && !jTextField_secundarioZ.getText().isEmpty() ){
                questao04();
            }
            else if(jRadioButton_q05.isSelected()){
                if(!jTextField_escalar.getText().isEmpty()){
                    questao05();
                }
                else{
                    JOptionPane.showMessageDialog(null,"Digite um valor na Área de texto ESCALAR");
                    jTextArea_resultado.setText("");            
                }
            }
            else if(jRadioButton_q06.isSelected()){
                if(!jTextField_escalar.getText().isEmpty()){
                    questao06();
                }
                else{
                    JOptionPane.showMessageDialog(null,"Digite um valor na Área de texto ESCALAR");
                    jTextArea_resultado.setText("");            
                }
            }
            else if(jRadioButton_q07.isSelected() && 
                    !jTextField_secundarioX.getText().isEmpty() && !jTextField_secundarioY.getText().isEmpty() && !jTextField_secundarioZ.getText().isEmpty()){
                questao07();
            }
            else {
                JOptionPane.showMessageDialog(null,"Digite valores no VETOR SECUNDARIO");
                jTextArea_resultado.setText("");            
            }
        }
        else{
            JOptionPane.showMessageDialog(null,"Digite valores no VETOR PRINCIPAL");
            jTextArea_resultado.setText("");            
        }
              
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        Form02 form02 = new Form02();
        form02.setVisible(true);
        setVisible(false);
    }//GEN-LAST:event_jButton2ActionPerformed

    public static void main(String args[]) {
        
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Form01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Form01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Form01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Form01.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        

        
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Form01().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.ButtonGroup buttonGroup_programa01;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JRadioButton jRadioButton_q01;
    private javax.swing.JRadioButton jRadioButton_q02;
    private javax.swing.JRadioButton jRadioButton_q03;
    private javax.swing.JRadioButton jRadioButton_q04;
    private javax.swing.JRadioButton jRadioButton_q05;
    private javax.swing.JRadioButton jRadioButton_q06;
    private javax.swing.JRadioButton jRadioButton_q07;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextArea jTextArea_resultado;
    private javax.swing.JTextField jTextField_escalar;
    private javax.swing.JTextField jTextField_principalX;
    private javax.swing.JTextField jTextField_principalY;
    private javax.swing.JTextField jTextField_principalZ;
    private javax.swing.JTextField jTextField_secundarioX;
    private javax.swing.JTextField jTextField_secundarioY;
    private javax.swing.JTextField jTextField_secundarioZ;
    // End of variables declaration//GEN-END:variables
}
