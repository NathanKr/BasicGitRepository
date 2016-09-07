using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ClassLibrary2
{
    public interface ProgressView
    {
        // --- info IN called by caller to provide info in
         void Set(InputInfo oInputInfo);

        // --- info OUT called by caller to know result - info out
         OutputInfo Get();


        void SetText(string strText);

        void ShowProgressBar(bool bShow);
        
        // --- e.g. combo box
        void ShowProgressDetails();
   
        void SetProgressValue(int nValue);
        void SetValueMinMax(int nValueMin,int nValueMax);
        
        void IncrementValue();

        void ShowCloseButton(bool bShow);
    }
}
