//find;

void initnet()

//add above;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
PyObject* netDungeonTeleport(PyObject* poSelf, PyObject* poArgs)
{
	int coordX;
	if (!PyTuple_GetInteger(poArgs, 0, &coordX))
		return Py_BuildException();

	int coordY;
	if (!PyTuple_GetInteger(poArgs, 1, &coordY))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.DungeonTeleport(coordX, coordY);
	return Py_BuildNone();
}
#endif

//find again;

		{ "RegisterErrorLog",						netRegisterErrorLog,						METH_VARARGS },

//add below;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
		{ "DungeonTeleport",						netDungeonTeleport,							METH_VARARGS },
#endif