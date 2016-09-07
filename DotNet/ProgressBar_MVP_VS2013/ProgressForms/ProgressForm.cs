using ClassLibrary2;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ProgressForms
{
    public partial class ProgressForm : Form, ProgressView
    {
        public ProgressForm()
        {
            ProgressPresnter m_ProgressPresenter =
                ProgressFactory.CreatePresenter(this, ProgressFactory.CreateModel());
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            m_ProgressPresenter.OnLoad();
        }




        public void Set(InputInfo oInputInfo)
        {
            throw new NotImplementedException();
        }

        public OutputInfo Get()
        {
            throw new NotImplementedException();
        }

        void ProgressView.SetText(string strText)
        {
            throw new NotImplementedException();
        }

        void ProgressView.ShowProgressBar(bool bShow)
        {
            throw new NotImplementedException();
        }

        void ProgressView.ShowProgressDetails()
        {
            throw new NotImplementedException();
        }

        void ProgressView.SetProgressValue(int nValue)
        {
            throw new NotImplementedException();
        }

        void ProgressView.SetValueMinMax(int nValueMin, int nValueMax)
        {
            throw new NotImplementedException();
        }

        void ProgressView.IncrementValue()
        {
            throw new NotImplementedException();
        }

        void ProgressView.ShowCloseButton(bool bShow)
        {
            throw new NotImplementedException();
        }

        ProgressPresnter m_ProgressPresenter;
    }
}
