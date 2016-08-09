
		
		var m_elShape = document.getElementById("shape"),
			m_elreactTimeMs = document.getElementById("reactTimeMs"),
			m_elplayground = document.getElementById("playground"),
			m_nRand, m_ShapeAppearedMs, m_nClickTimeMs;
		
		pick_TopLeft_Color_Shape();
		startTimer();
		
		// --- ranom integer on range nStart,nEnd including
		function GetRandomInteger(nStart,nEnd)
		{
			return Math.floor(Math.random() * (nEnd - nStart+1)) + nStart;
		}
		
		m_elShape.onclick = function()
		{
			stopTimer();
			showTimeDiff();
			pick_TopLeft_Color_Shape();
			startTimer();
		}		
		


		function pick_TopLeft_Color_Shape()
		{
			pickTopLeft();
			pickColor();
			pickShape();
			
		}
		
		function pickTopLeft()
		{
			m_elShape.style.top = 
			GetRandomInteger(0,m_elplayground.clientHeight - m_elShape.clientHeight)+"px";
			
			m_elShape.style.left = 
			GetRandomInteger(0,m_elplayground.clientWidth - m_elShape.clientWidth)+"px";
		}
		
		function pickColor()
		{
			m_nRand = GetRandomInteger(0,2);
			var strColor;
			
			switch(m_nRand) 
			{
				case 0:
					strColor="red";
				break;
    
				case 1:
					strColor="blue";
				break;
    
			default:
				strColor="green";
			}
			
			m_elShape.style.background = strColor;
		}
		
		function pickShape()
		{
			m_nRand = GetRandomInteger(0,1);
			console.log(m_nRand);
			
			if(m_nRand == 1)
			{
				setCircle();
			}
			else
			{
				setSquare();
			}
		}
		
		function setCircle()
		{
			m_elShape.style.borderRadius = "50%";
		}
		
		function setSquare()
		{
			m_elShape.style.borderRadius = "0";
		}
		
		function startTimer()
		{
			m_ShapeAppearedMs = new Date().getTime();
		}
		
		function stopTimer()
		{
			m_nClickTimeMs = new Date().getTime() - m_ShapeAppearedMs;
		}
		
		function showTimeDiff()
		{
			m_elreactTimeMs.innerHTML = m_nClickTimeMs/1000;
		}	

		
			
		