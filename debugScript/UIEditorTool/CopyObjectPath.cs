// **********************************************************************
// Copyright(C) by Lakoo
// FileName:     CopyObjectPath.cs
// Author:       zezhang
// UnityVersion：2019.4.6f1
// Date:         2020-12-14
// Purpose:      copy prefab gameObject path
// **********************************************************************


using UnityEditor;
using UnityEngine;

using LuaInterface;
using System;


#if UNITY_EDITOR
public class CopyObjectPath:EditorWindow
{

    [MenuItem("GameObject/Copy Object Path _C", priority = -1)]
    static void CopyPath()
    {

            GameObject selectObj = Selection.activeGameObject;
            RectTransform[] list = selectObj.GetComponentsInParent<RectTransform>();
            string path = string.Empty;
            if (list.Length >= 3)
            {
                for (int i = list.Length - 3; i >= 0; i--)
                {
                    if (string.IsNullOrEmpty(path))
                        path = list[i].name;
                    else
                        path += "/" + list[i].name;
                }
            }
            else
            {
                path = selectObj.name;
            }

            GUIUtility.systemCopyBuffer = path;
            Debug.Log("copy path=" + path);
    }




    [MenuItem("reload lua file/reload")]
    static void ReroadLua()
    {

        LuaState luaState = LuaClient.Instance.GetLuaState();
        luaState.DoFile("Debug/Debug.lua");
        
    }
}
#endif
