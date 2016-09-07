using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ClassLibrary2
{
    public interface ProgressPresnter
    {
        // --- called inside view load
        void OnLoad();

        // --- called inside close click
        void OnCloseClick();
    }
}
