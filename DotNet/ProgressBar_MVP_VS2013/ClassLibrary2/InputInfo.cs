using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ClassLibrary2
{
    public enum ProgressType
    {
        Circuler,
        NonCircular
    }

    public class InputInfo
    {
        public string strText;
        public bool bShowProgressDetails;
        public bool bShowCloseButton;
        public ProgressType type;
    }
}
