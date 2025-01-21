from PyQt5.QtWidgets import QPushButton


class OrangeCustomButton(QPushButton):
    def __init__(self, btn_text):
        super().__init__(btn_text)
        self.setStyleSheet(
            """ 
            QPushButton{
              background: #FF4742;
              border: 1px solid #FF4742;
              border-radius: 6px;
              box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
              box-sizing: border-box;
              color: #FFFFFF;
              cursor: pointer;
              display: inline-block;
              font-family: nunito,roboto,proxima-nova,"proxima nova",sans-serif;
              font-size: 16px;
              font-weight: 800;
              line-height: 16px;
              min-height: 40px;
              outline: 0;
              padding: 12px 14px;
              text-align: center;
              text-rendering: geometricprecision;
              text-transform: none;
              user-select: none;
              -webkit-user-select: none;
              touch-action: manipulation;
              vertical-align: middle;
            }
            
            QPushButton:hover{
              background-color: white;
              background-position: 0 0;
              color: #FF4742;
            }
            """
        )
