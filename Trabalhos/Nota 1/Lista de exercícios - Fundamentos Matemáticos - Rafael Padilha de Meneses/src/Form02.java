import javax.swing.JOptionPane;
import javax.swing.JTable;
/*
   Programa 02 - Desenvolva um programa que leia pelo teclado os valores de uma matriz 3x3, e então apresente um menu com as seguintes opções:
   1 -> Adição e subtração de outra matriz, lendo os valores dessa outra matriz 3x3 e mostrando o resultado na tela;
   2 -> Multiplicação e Divisão de um escalar lido pelo teclado;
   3 -> Multiplicação da matriz por um vetor de 3 elementos, este lido pelo teclado;
   4 -> Multiplicação da matriz por outra matriz 3x3, esta lida pelo teclado;
   5 -> Apresentar a transposta da matriz lida inicialmente.
 */
public class Form02 extends javax.swing.JFrame {
    
    public Form02() {
        initComponents();
        jRadioButton_q01.setSelected(true);
        setLocationRelativeTo(null);
    }
    
    public boolean verificarTabela(JTable tabela){
        
        int contadorErros = 0;
        
        for (int i = 0; i < 3 ; i++) {
            for (int j = 0; j < 3 ; j++) {               
                if(tabela.getValueAt(i,j)==null){
                    contadorErros++;                   
                }              
            }           
        }
        if(contadorErros==0){
            return false;
        }
        else{
            return true;
        }
    }
    
    public void limparTabelas(JTable tabela){
        for (int i = 0; i < 3 ; i++) {
                for (int j = 0; j < 3 ; j++) {
                    tabela.setValueAt(null, i, j);                
                }           
            }          
    }
    
    public void questao01(){
            
        Object[] options = {"Somar", "Subtrair"};
        int n = JOptionPane.showOptionDialog(null,
            "Qual operação?",
            "Selecionar Operação",
            JOptionPane.YES_NO_OPTION,
            JOptionPane.QUESTION_MESSAGE,
            null,     
            options,  
            options[0]);
        
        if(n==0){
            for (int i = 0; i < 3 ; i++) {
                for (int j = 0; j < 3 ; j++) {
                    jTable_resultante.setValueAt( ((double)jTable_principal.getValueAt(i, j)+(double)jTable_secundaria.getValueAt(i, j)) , i, j);                
                }           
            }         
        }
        else if(n==1){
            for (int i = 0; i < 3 ; i++) {
                for (int j = 0; j < 3 ; j++) {
                    jTable_resultante.setValueAt( ((double)jTable_principal.getValueAt(i, j)-(double)jTable_secundaria.getValueAt(i, j)) , i, j);                
                }           
            }
        }
        else{
            JOptionPane.showMessageDialog(null,"Nenhuma opção foi selecionada");
        }              
    }
    
    public void questao02(){
        
        Object[] options = {"Multiplicar", "Dividir"};
        int n = JOptionPane.showOptionDialog(null,
            "Qual operação?",
            "Selecionar Operação",
            JOptionPane.YES_NO_OPTION,
            JOptionPane.QUESTION_MESSAGE,
            null,     
            options,  
            options[0]);
        
        if(n==0){
            for (int i = 0; i < 3 ; i++) {
                for (int j = 0; j < 3 ; j++) {
                    jTable_resultante.setValueAt(  (double)jTable_principal.getValueAt(i, j) * (Double.parseDouble(jTextField_escalar.getText())), i , j );                
                }           
            }
        }
        else if(n==1){
            for (int i = 0; i < 3 ; i++) {
                for (int j = 0; j < 3 ; j++) {
                    jTable_resultante.setValueAt(  (double)jTable_principal.getValueAt(i, j) / (Double.parseDouble(jTextField_escalar.getText())), i , j );                
                }           
            }
        }
        else{
            JOptionPane.showMessageDialog(null,"Nenhuma opção foi selecionada");
        }   
    }
    
    public void questao03(){
        
        limparTabelas(jTable_resultante);
        for (int i = 0; i < 3 ; i++) { // row                     
            for (int j = 0; j < 3 ; j++) { // column
                jTable_resultante.setValueAt( (  (double)jTable_principal.getValueAt( i, 0 ) * (Double.parseDouble(jTextField_vetorX.getText())) ) 
                        + (double)jTable_principal.getValueAt( i, 1 ) * (Double.parseDouble(jTextField_vetorY.getText()))
                        + (double)jTable_principal.getValueAt( i, 2 ) * (Double.parseDouble(jTextField_vetorZ.getText())) 
                        , i , 0 );               
            }           
        }
        
    }
    
    public void questao04(){
        for (int i = 0; i < 3 ; i++) { // row                     
            for (int j = 0; j < 3 ; j++) { // column
                jTable_resultante.setValueAt( (  (double)jTable_principal.getValueAt( i, 0 ) * (double)jTable_secundaria.getValueAt( 0, j ) ) 
                        + (double)jTable_principal.getValueAt( i, 1 ) * (double)jTable_secundaria.getValueAt( 1, j )
                        + (double)jTable_principal.getValueAt( i, 2 ) * (double)jTable_secundaria.getValueAt( 2, j ) 
                        , i , j );               
            }           
        }
    }
    
    public void questao05(){
        for (int i = 0; i < 3 ; i++) { // row                     
            for (int j = 0; j < 3 ; j++) { // column
                jTable_resultante.setValueAt(jTable_principal.getValueAt(i, j), j, i);
            }           
        }
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        jRadioButton_q04 = new javax.swing.JRadioButton();
        jScrollPane9 = new javax.swing.JScrollPane();
        jTable_principal = new javax.swing.JTable();
        jRadioButton_q05 = new javax.swing.JRadioButton();
        jRadioButton_q01 = new javax.swing.JRadioButton();
        jRadioButton_q02 = new javax.swing.JRadioButton();
        jScrollPane7 = new javax.swing.JScrollPane();
        jTable_secundaria = new javax.swing.JTable();
        jRadioButton_q03 = new javax.swing.JRadioButton();
        jScrollPane8 = new javax.swing.JScrollPane();
        jTable_resultante = new javax.swing.JTable();
        jTextField_escalar = new javax.swing.JTextField();
        jLabel1 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jButton_calcular = new javax.swing.JButton();
        jLabel5 = new javax.swing.JLabel();
        jPanel1 = new javax.swing.JPanel();
        jTextField_vetorZ = new javax.swing.JTextField();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jTextField_vetorX = new javax.swing.JTextField();
        jTextField_vetorY = new javax.swing.JTextField();
        jButton1 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Programa 02");

        buttonGroup1.add(jRadioButton_q04);
        jRadioButton_q04.setText("4 -> Multiplicação da matriz Principal pela Secundária;");

        jTable_principal.setBackground(new java.awt.Color(204, 204, 204));
        jTable_principal.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(153, 0, 153), 2));
        jTable_principal.setFont(new java.awt.Font("Times New Roman", 0, 18)); // NOI18N
        jTable_principal.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null},
                {null, null, null},
                {null, null, null}
            },
            new String [] {
                "", "", ""
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Double.class, java.lang.Double.class, java.lang.Double.class
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }
        });
        jTable_principal.setAutoscrolls(false);
        jTable_principal.setGridColor(new java.awt.Color(153, 0, 153));
        jTable_principal.setRowHeight(25);
        jTable_principal.setRowSelectionAllowed(false);
        jTable_principal.setSelectionBackground(new java.awt.Color(204, 255, 255));
        jTable_principal.setShowGrid(true);
        jTable_principal.setTableHeader(null);
        jScrollPane9.setViewportView(jTable_principal);

        buttonGroup1.add(jRadioButton_q05);
        jRadioButton_q05.setText("5 -> Apresentar a transposta da matriz Principal.");

        buttonGroup1.add(jRadioButton_q01);
        jRadioButton_q01.setText("1 -> Adição e subtração da matriz Principal com a Secundária;");

        buttonGroup1.add(jRadioButton_q02);
        jRadioButton_q02.setText("2 -> Multiplicação e Divisão de um escalar, com a Principal;");

        jTable_secundaria.setBackground(new java.awt.Color(204, 204, 204));
        jTable_secundaria.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(153, 51, 0), 2));
        jTable_secundaria.setFont(new java.awt.Font("Times New Roman", 0, 18)); // NOI18N
        jTable_secundaria.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null},
                {null, null, null},
                {null, null, null}
            },
            new String [] {
                "", "", ""
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Double.class, java.lang.Double.class, java.lang.Double.class
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }
        });
        jTable_secundaria.setAutoscrolls(false);
        jTable_secundaria.setGridColor(new java.awt.Color(153, 51, 0));
        jTable_secundaria.setRowHeight(25);
        jTable_secundaria.setRowSelectionAllowed(false);
        jTable_secundaria.setSelectionBackground(new java.awt.Color(204, 255, 255));
        jTable_secundaria.setSelectionForeground(new java.awt.Color(0, 204, 204));
        jTable_secundaria.setShowGrid(true);
        jTable_secundaria.setTableHeader(null);
        jScrollPane7.setViewportView(jTable_secundaria);

        buttonGroup1.add(jRadioButton_q03);
        jRadioButton_q03.setText("3 -> Multiplicação da matriz Principal por um vetor de 3 elementos;");

        jTable_resultante.setBackground(new java.awt.Color(204, 204, 204));
        jTable_resultante.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(51, 153, 0), 2));
        jTable_resultante.setFont(new java.awt.Font("Times New Roman", 0, 18)); // NOI18N
        jTable_resultante.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null},
                {null, null, null},
                {null, null, null}
            },
            new String [] {
                "", "", ""
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Double.class, java.lang.Double.class, java.lang.Double.class
            };
            boolean[] canEdit = new boolean [] {
                false, false, false
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jTable_resultante.setAutoscrolls(false);
        jTable_resultante.setGridColor(new java.awt.Color(51, 153, 0));
        jTable_resultante.setRowHeight(25);
        jTable_resultante.setRowSelectionAllowed(false);
        jTable_resultante.setSelectionBackground(new java.awt.Color(204, 255, 255));
        jTable_resultante.setShowGrid(true);
        jTable_resultante.setTableHeader(null);
        jScrollPane8.setViewportView(jTable_resultante);

        jLabel1.setText("Matriz Principal");

        jLabel3.setText("Matriz Secundária");

        jLabel4.setText("Matriz Resultante");

        jButton_calcular.setText("Calcular");
        jButton_calcular.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton_calcularActionPerformed(evt);
            }
        });

        jLabel5.setText("Escalar");

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createMatteBorder(3, 3, 3, 3, new java.awt.Color(153, 0, 153)), "Vetor"));

        jLabel6.setText("Variavel X");

        jLabel7.setText("Variavel Y");

        jLabel8.setText("Variavel Z");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel6)
                    .addComponent(jTextField_vetorX, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel7)
                    .addComponent(jTextField_vetorY, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel8)
                    .addComponent(jTextField_vetorZ, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addComponent(jLabel6)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextField_vetorX, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel7)
                .addGap(5, 5, 5)
                .addComponent(jTextField_vetorY, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel8)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jTextField_vetorZ, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        jButton1.setText("Programa 01");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jButton2.setText("Limpar");
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
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(10, 10, 10)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel1)
                            .addComponent(jScrollPane9, javax.swing.GroupLayout.PREFERRED_SIZE, 182, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel3)
                            .addComponent(jScrollPane7, javax.swing.GroupLayout.PREFERRED_SIZE, 182, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel4)
                            .addComponent(jScrollPane8, javax.swing.GroupLayout.PREFERRED_SIZE, 182, javax.swing.GroupLayout.PREFERRED_SIZE))))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jRadioButton_q01)
                            .addComponent(jRadioButton_q03)
                            .addComponent(jRadioButton_q02)
                            .addComponent(jRadioButton_q04)
                            .addComponent(jRadioButton_q05)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(4, 4, 4)
                                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(jButton_calcular, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(jLabel5, javax.swing.GroupLayout.PREFERRED_SIZE, 50, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jTextField_escalar)
                                    .addComponent(jButton2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
                        .addContainerGap(27, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jButton1)
                        .addGap(37, 37, 37))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addComponent(jRadioButton_q01)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q02)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q03)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q04)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jRadioButton_q05)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(jButton1))
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addGap(18, 18, 18)
                                        .addComponent(jLabel5, javax.swing.GroupLayout.PREFERRED_SIZE, 20, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGap(0, 0, 0)
                                        .addComponent(jTextField_escalar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGap(18, 18, 18)
                                        .addComponent(jButton_calcular)
                                        .addGap(18, 18, 18)
                                        .addComponent(jButton2))
                                    .addGroup(layout.createSequentialGroup()
                                        .addGap(12, 12, 12)
                                        .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                .addGap(0, 0, Short.MAX_VALUE))))
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addComponent(jLabel1)
                        .addGap(6, 6, 6)
                        .addComponent(jScrollPane9, javax.swing.GroupLayout.PREFERRED_SIZE, 81, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel3)
                        .addGap(6, 6, 6)
                        .addComponent(jScrollPane7, javax.swing.GroupLayout.PREFERRED_SIZE, 81, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel4)
                        .addGap(6, 6, 6)
                        .addComponent(jScrollPane8, javax.swing.GroupLayout.PREFERRED_SIZE, 81, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(0, 30, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton_calcularActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton_calcularActionPerformed
          
        if(verificarTabela(jTable_principal)==false){
            
            if(jRadioButton_q01.isSelected() && verificarTabela(jTable_secundaria)==false){
                questao01();
            }
            else if(jRadioButton_q02.isSelected()){
                if(!jTextField_escalar.getText().isBlank()){
                    questao02();
                }
                else{
                    JOptionPane.showMessageDialog(null,"Preencher a Área de texto do ESCALAR");
                }
            }
            else if(jRadioButton_q03.isSelected()){               
                if(!jTextField_vetorX.getText().isEmpty() && !jTextField_vetorY.getText().isEmpty() && !jTextField_vetorZ.getText().isEmpty()){
                    questao03();
                }
                else{
                    JOptionPane.showMessageDialog(null,"Preencher o Vetor");
                }            
            }
            else if(jRadioButton_q04.isSelected() && verificarTabela(jTable_secundaria)==false){
                questao04();               
            }
            else if(jRadioButton_q05.isSelected()){
                questao05();
            }
            else{
                JOptionPane.showMessageDialog(null,"Completar a MATRIZ SECUNDARIA\n(Se alguma celula estivar destacada em branco,\nbasta apertar 'enter')");
            }           
        }
        else{
            JOptionPane.showMessageDialog(null,"Completar a MATRIZ PRINCIPAL\n(Se alguma celula estivar destacada em branco,\nbasta apertar 'enter')");
        }    
    }//GEN-LAST:event_jButton_calcularActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        Form01 form01 = new Form01();
        form01.setVisible(true);
        setVisible(false);
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        
        Object[] options = {"Sim", "Não"};
        int n = JOptionPane.showOptionDialog(null,
            "Deseja limpar as três MATRIZES, o VETOR e o ESCALAR?",
            "Selecionar Operação",
            JOptionPane.YES_NO_OPTION,
            JOptionPane.QUESTION_MESSAGE,
            null,     
            options,  
            options[0]);
        
        if(n==0){
            limparTabelas(jTable_principal);
            limparTabelas(jTable_secundaria);
            limparTabelas(jTable_resultante);
            jTextField_vetorX.setText("");
            jTextField_vetorY.setText("");
            jTextField_vetorZ.setText("");
            jTextField_escalar.setText("");
        }
        else{
            JOptionPane.showMessageDialog(null,"Nenhum lugar foi limpo");
        }
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
            java.util.logging.Logger.getLogger(Form02.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Form02.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Form02.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Form02.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
           
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Form02().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton_calcular;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JRadioButton jRadioButton_q01;
    private javax.swing.JRadioButton jRadioButton_q02;
    private javax.swing.JRadioButton jRadioButton_q03;
    private javax.swing.JRadioButton jRadioButton_q04;
    private javax.swing.JRadioButton jRadioButton_q05;
    private javax.swing.JScrollPane jScrollPane7;
    private javax.swing.JScrollPane jScrollPane8;
    private javax.swing.JScrollPane jScrollPane9;
    private javax.swing.JTable jTable_principal;
    private javax.swing.JTable jTable_resultante;
    private javax.swing.JTable jTable_secundaria;
    private javax.swing.JTextField jTextField_escalar;
    private javax.swing.JTextField jTextField_vetorX;
    private javax.swing.JTextField jTextField_vetorY;
    private javax.swing.JTextField jTextField_vetorZ;
    // End of variables declaration//GEN-END:variables
}
